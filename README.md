# Amazon Price Tracker and Notifier

## Project Description
This project contains a Python script that monitors the price and rating of a specific product on Amazon. When the rating of the product is above a defined threshold, it triggers an automated email alert to inform the user of the high-rated product. Additionally, the script logs the product title, its rating, and the current date to a CSV file for historical tracking.

## Features
- **Web Scraping**: Utilizes `BeautifulSoup` to parse Amazon product pages.
- **Data Logging**: Stores product details in a CSV file for future analysis.
- **Email Notifications**: Sends emails via `smtplib` when a product meets the desired criteria.

## Usage
1. Clone the repository.
2. Install the required dependencies: `requests`, `beautifulsoup4`, and `pandas`.
3. Set your product URL, email credentials, and desired rating threshold within the script.
4. Run the script with Python to begin tracking.

## Requirements
- Python 3
- `requests`
- `beautifulsoup4`
- `pandas`
- `smtplib`

## Setup and Configuration
Before running the script, update the following variables in the script:
- `url`: URL of the Amazon product to track.
- `headers`: Update the User-Agent to a value that corresponds to your browser.
- Email credentials within the `send_mail` function for email functionality.

**Note**: Use environment variables or other secure methods to handle sensitive data like email credentials.

## Disclaimer
This script is for educational purposes only. Web scraping can be against the Terms of Service of some websites. Use this script responsibly and ethically. Always ensure you comply with Amazon's terms of service when using this tool.

## Contribution
Contributions are welcome. Please feel free to submit a pull request or create an issue for any bugs or enhancements.

