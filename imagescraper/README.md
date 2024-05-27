## Image Scraper Tool

This Python-based tool automates the process of downloading images from websites using Selenium and Requests libraries. It is designed to handle both simple and complex scenarios including dynamic content loading, session management, and handling rate limits with retries.

### Features
- **Dynamic Image Scraping**: Scrolls through web pages to load and capture all available images.
- **Session Management**: Maintains session data across requests, which is essential for accessing pages that require login.
- **Rate Limit Handling**: Implements retry strategies with exponential backoff to manage HTTP 429 (Too Many Requests) responses effectively.
- **Robust Image Downloading**: Downloads images in chunks to handle large files efficiently without overloading memory.

### Prerequisites
- Python 3.x
- Selenium WebDriver
- Requests library
- BeautifulSoup (for parsing HTML content)
- urllib3 (for retry strategy)

### Setup
1. **Install Python Libraries**:
   ```bash
   pip install selenium requests beautifulsoup4 urllib3
   ```

2. **WebDriver**:
   Ensure you have a WebDriver installed (e.g., ChromeDriver or GeckoDriver) that matches the version of your browser. This driver should be accessible in your system's PATH, or you can specify the path directly in the script.

### Usage
1. **Configuration**: Edit the script to include the URL of the website, download path, and login credentials (if necessary).
2. **Run the Script**:
   ```bash
   python image_scraper.py
   ```
   Follow the prompts to enter the website URL and login details (if required).

### How It Works
- **Image Scraping**: The script uses Selenium to navigate and scroll through the webpage, ensuring all images are loaded. Images are then captured and downloaded using Requests.
- **Session Cookies**: A session object in Requests reuses the HTTP connection for multiple requests, which not only speeds up the process but also maintains cookies across all requests, crucial for pages requiring authentication.
- **Downloading Images**: Images are downloaded in 1024-byte chunks, which allows the script to handle large images efficiently and reduce memory usage.
- **Retry Mechanism**: The script retries failed downloads, particularly useful when encountering rate limits (HTTP 429 errors). It respects the `Retry-After` header to pause requests accordingly.

### Handling Failures
- The script includes error handling for network issues and server errors. It logs the status and skips over images that cannot be retrieved after the maximum retry count is reached.

### Output
- Images are saved to the specified directory. Each image is named sequentially (e.g., `img1.jpg`, `img2.jpg`, etc.).

### Troubleshooting
- Ensure that the WebDriver version matches your browser version.
- Check network connectivity if downloads fail.
- Verify that the specified folder path for downloads exists and is writable.

### Note
This tool is intended for educational and legitimate usage only. Users should ensure they have permission to scrape images from any website and respect robots.txt and terms of service.