import socket
from collections import defaultdict
from datetime import datetime, timedelta


class BasicIDS:
    def __init__(self, host="0.0.0.0", port=5000, threshold=10):
        self.host = host
        self.port = port
        self.threshold = threshold  # Threshold for connection attempts from the same IP
        self.connections = defaultdict(list)  # Store timestamped connection attempts

    def monitor_connections(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(5)
            print(f"Listening on {self.host}:{self.port}...")

            while True:
                client_socket, addr = s.accept()
                now = datetime.now()
                ip = addr[0]
                print(f"Connection from {ip} at {now.strftime('%Y-%m-%d %H:%M:%S')}")

                # Log the connection
                self.log_connection(ip, now)
                self.check_for_attacks(ip, now)

                client_socket.close()

    def log_connection(self, ip, timestamp):
        self.connections[ip].append(timestamp)

    def check_for_attacks(self, ip, timestamp):
        recent_connections = [
            t for t in self.connections[ip] if timestamp - t < timedelta(seconds=30)
        ]
        if len(recent_connections) > self.threshold:
            print(
                f"Potential attack detected: {len(recent_connections)} connections from {ip} in the last minute"
            )


if __name__ == "__main__":
    ids = BasicIDS(port=5000)  # Initialize IDS
    ids.monitor_connections()
