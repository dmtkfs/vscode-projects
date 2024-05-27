from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
import hashlib


def setup_driver():
    driver = webdriver.Firefox()  # Adjust for your preferred browser
    driver.maximize_window()
    return driver


def scroll_and_save_images(driver, url, download_path):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    image_count = 0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Allow time for the page to load new images

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # No new content loaded, stop scrolling
        last_height = new_height

        images = driver.find_elements(By.TAG_NAME, "img")
        image_count = save_images(images, download_path, image_count)

    print(f"Total number of images downloaded: {image_count}")


def save_images(images, download_path, image_count):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for image in images:
        src = image.get_attribute("src")
        if src and src.startswith("http"):
            file_name = filename_from_url(src, image_count)
            file_path = os.path.join(download_path, file_name)
            if download_image(src, file_path):
                image_count += 1
    return image_count


def filename_from_url(url, index):
    # Create a unique filename using MD5 hash of the URL with index as a prefix
    hash_object = hashlib.md5(url.encode())
    return f"{index}_{hash_object.hexdigest()}.jpg"


def download_image(src, file_path):
    try:
        response = requests.get(src, stream=True, timeout=10)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(8192):
                    f.write(chunk)
            print(f"Downloaded: {src}")
            return True
        else:
            print(f"Failed to download {src}, HTTP status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error downloading {src}: {e}")
    return False


if __name__ == "__main__":
    url = input("Enter the webpage URL: ")
    download_path = os.path.expanduser("~/Desktop/downloaded_images")

    driver = setup_driver()
    scroll_and_save_images(driver, url, download_path)
    driver.quit()
