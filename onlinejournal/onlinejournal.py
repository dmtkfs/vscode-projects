import sys
import json
import struct
import os
import logging
import traceback

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    filename="onlinejournal.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DEBUG_FILE = "debug.log"


def send_message(message):
    encoded_message = json.dumps(message).encode("utf-8")
    sys.stdout.buffer.write(struct.pack("I", len(encoded_message)) + encoded_message)
    sys.stdout.buffer.flush()


def receive_message():
    with open(DEBUG_FILE, "a") as f:
        f.write("receive_message called\n")
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack("I", raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    with open(DEBUG_FILE, "a") as f:
        f.write(f"Received raw message: {message}\n")
    logging.info(f"Received message: {message}")
    return json.loads(message)


def secure_filename(filename):
    return os.path.basename(filename)


def save_file(file_path, content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        logging.info(f"File saved successfully: {file_path}")
        return True
    except Exception as e:
        logging.error(f"Failed to save file: {file_path}, Error: {str(e)}")
        traceback.print_exc()
        return False


def main():
    with open(DEBUG_FILE, "a") as f:
        f.write("main called\n")
    while True:
        message = receive_message()
        with open(DEBUG_FILE, "a") as f:
            f.write(f"Message received: {message}\n")
        if "filename" in message and "content" in message:
            filename = secure_filename(message["filename"])
            downloads_folder = os.path.join(
                os.getenv("USERPROFILE") or os.getenv("HOME"), "Downloads"
            )
            archived_pages_folder = os.path.join(downloads_folder, "ArchivedPages")
            filepath = os.path.join(archived_pages_folder, filename)
            success = save_file(filepath, message["content"])
            send_message({"success": success})


if __name__ == "__main__":
    with open(DEBUG_FILE, "a") as f:
        f.write("__main__ executed\n")
    main()
