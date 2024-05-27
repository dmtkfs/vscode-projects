from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import random
import time
import requests
import os


def scroll_and_save_images(driver, url):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    image_count = 0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
        )

        images = driver.find_elements(By.TAG_NAME, "img")
        for image in images[
            image_count:
        ]:  # Start from the last count to avoid duplicates
            src = image.get_attribute("src")
            if src and src.startswith("http"):
                image_count += 1
                image_name = f"img{image_count}.jpg"
                download_image(src, os.path.join(download_path, image_name))

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    print("Total number of images downloaded:", image_count)


def login(driver, username, password):
    driver.get(url)
    username_field = driver.find_element(By.ID, "username_field_id")
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "password_field_id")
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, "login_button_id")
    login_button.click()
    time.sleep(2)


def download_image(url, file_path):
    retry_strategy = Retry(
        total=10,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=[
            "HEAD",
            "GET",
            "OPTIONS",
        ],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
        else:
            print(f"Failed to download {url}, status code {response.status_code}")
            if response.status_code == 429:
                retry_after = int(
                    response.headers.get("Retry-After", 60)
                )  # Use header or default to 60 seconds
                print(f"Rate limit hit, sleeping for {retry_after} seconds")
                time.sleep(retry_after)  # Respect the Retry-After header
    except Exception as e:
        print(f"Exception occurred while downloading {url}: {e}")
    finally:
        session.close()
    time.sleep(random.uniform(1, 3))  # Random sleep between 1 and 3 seconds


if __name__ == "__main__":
    url = input("Give the webpage url: ")
    download_path = os.path.expanduser("~/Desktop/downloaded_images")

    login_required = input("Do you want to login? (y/n) ")
    driver = webdriver.Firefox()  # Initialize the driver
    if login_required.lower() == "y":
        username = input("Give your username: ")
        password = input("Give your password: ")
        login(driver, username, password)
    else:
        print("Continuing without login.")

    scroll_and_save_images(driver, url)
    driver.quit()
