This Python script scrapes the list of largest companies in the United States by revenue from Wikipedia and saves it into a CSV file for easy analysis

Features

Requests the Wikipedia page containing the list of largest US companies by revenue.

Parses the HTML content using BeautifulSoup.

Extracts key information including:

Rank

Company Name

Industry

Revenue

Revenue Growth

Headquarters

Saves the extracted data into a CSV file (largest_us_companies.csv).

Requirements

This project requires Python 3.7+ and the following Python packages:

requests

beautifulsoup4

pandas
