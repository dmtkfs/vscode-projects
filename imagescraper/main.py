from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os


def setup_driver():
    driver = (
        webdriver.Firefox()
    )  # Ensure geckodriver is in your PATH or specify the path
    driver.maximize_window()
    return driver


def scroll_and_save_images(driver, url, download_path):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Sleep to allow page to load

        # Attempt to find new images
        images = driver.find_elements(By.TAG_NAME, "img")
        download_images(images, download_path)

        # Check if the scroll has reached the bottom of the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def download_images(images, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for index, image in enumerate(images):
        src = image.get_attribute("src")
        if src and src.startswith("http"):
            file_path = os.path.join(download_path, f"image_{index + 1}.jpg")
            try:
                response = requests.get(src, stream=True)
                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        for chunk in response.iter_content(8192):
                            f.write(chunk)
                    print(f"Downloaded {src}")
            except requests.RequestException as e:
                print(f"Failed to download {src}: {e}")


if __name__ == "__main__":
    url = input("Enter the webpage URL: ")
    download_path = os.path.expanduser("~/Desktop/downloaded_images")

    driver = setup_driver()
    scroll_and_save_images(driver, url, download_path)
    driver.quit()
