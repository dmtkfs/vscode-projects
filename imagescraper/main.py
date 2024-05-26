from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

# Configuration
url = "http://test.com/login"
username = "xxx"
password = "xxxx"
image_page_url = "http://test.com/images"
download_path = os.path.expanduser("~/Desktop/downloaded_images")

"""If geckodriver is not in your PATH, specify the executable_path:
driver = webdriver.Firefox(executable_path='path_to_geckodriver'), else leave comment"""
driver = webdriver.Firefox()


def login():
    driver.get(url)

    # Find the username field
    username_field = driver.find_element(By.ID, "username_field_id")
    username_field.send_keys(username)

    # Find the password field
    password_field = driver.find_element(By.ID, "password_field_id")
    password_field.send_keys(password)

    # Find the login button
    login_button = driver.find_element(By.ID, "login_button_id")
    login_button.click()

    time.sleep(2)  # Wait for login


def scrape_images():
    driver.get(image_page_url)
    images = driver.find_elements(By.TAG_NAME, "img")

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    image_count = 0
    for image in images:
        src = image.get_attribute("src")
        image_name = src.split("/")[-1]  # Extract the image name
        print(image_name)  # Print the image name
        download_image(src, os.path.join(download_path, image_name))
        image_count += 1

    print("Total number of images:", image_count)


def download_image(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)


if __name__ == "__main__":
    login()
    scrape_images()
    driver.quit()
