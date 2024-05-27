## Simple Image Scraper Tool

This Python script uses Selenium to automate the process of scrolling through a webpage and downloading all visible images. It is designed for simplicity and ease of use, suitable for general web scraping tasks.

### Features

- **Automated Web Browsing**: Uses Selenium WebDriver to navigate web pages.
- **Image Downloading**: Downloads every visible image on the webpage.
- **Simple and Effective**: Focuses on fundamental functionalities making it robust across various websites.

### Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.x
- Selenium WebDriver
- Requests library

### Installation

1. **Install Required Python Libraries**:
   ```bash
   pip install selenium requests
   ```

2. **WebDriver Setup**:
   Download and install WebDriver for your browser (e.g., ChromeDriver for Google Chrome, GeckoDriver for Firefox). Ensure it is placed in your PATH or specify its path in the script.

### Usage Instructions

1. **Modify the Script**: 
   - Open the script in a text editor.
   - Modify the `url` variable to point to the desired webpage.
   - Update the `download_path` variable to your preferred download location.

2. **Run the Script**:
   Open a terminal or command prompt and run:
   ```bash
   python image_scraper.py
   ```
   The script will open the specified webpage, scroll through it, and download all images.

### Script Overview

- **Setup Driver**: Initializes the Selenium WebDriver for the specified browser.
- **Scroll and Save Images**: Scrolls through the webpage, captures all images, and downloads them to a specified directory.
- **Image Download Functionality**: Handles the image downloading in chunks to manage memory efficiently and accommodate large images.

### How It Works

The script operates by:
- Opening the target webpage using Selenium WebDriver.
- Continuously scrolling to the bottom until no new page content loads.
- Locating all `<img>` tags and fetching their `src` attributes.
- Downloading each image from its source URL to the specified directory.

### Troubleshooting

- **Script Doesn't Start**: Ensure WebDriver is correctly installed and its path is properly configured in the script.
- **Images Not Downloading**: Check network permissions and the validity of image URLs.
- **WebDriver Issues**: Make sure that the WebDriver version is compatible with your browser version.

### Note

This tool is designed for educational purposes and straightforward scraping tasks. Always ensure that you are in compliance with website terms of service and legal requirements when scraping data.