
# Problem Statement:

# The task is to scrape the list of largest companies in US by revenue from wikipedia 
# using Beautiful Soup in Python. The data required to be extracted 
# includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

# Question:

# What is the process to extract data from the wikipedia website using Beautiful Soup in Python?
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth, 
# Headquarters for the top US companies by Revenue?

import requests
from bs4 import BeautifulSoup
import pandas as pd



# Requesting the webpage(wikipedia)
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

#Add headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code != 200:
    raise Exception(f"Failed to retrieve page: Status code {response.status_code}")

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Locating the table containing the company data
# Find the largest companies in US by revenue table
table = soup.find('table', {'class':'wikitable sortable'})
if not table:
    raise Exception("the list of largest companies in US by revenue from wikipedia")

# Extract the relevant table columns
rows = table.find_all('tr')

# Extract Required columns
data = []

for row in rows[1:]:  # Skip header row
    cols = row.find_all('td')  
    if len(cols) >= 6:
        rank = cols[0].text.strip()
        company = cols[1].text.strip()
        industry = cols[2].text.strip()
        revenue = cols[3].text.strip()
        revenue_growth = cols[4].text.strip()
        headquarters = cols[5].text.strip()
        data.append([rank, company, industry, revenue, revenue_growth, headquarters])

# Create DataFrame
df = pd.DataFrame(data, columns=['Rank','Company','Industry','Revenue','Revenue_Growth','Headquarters'])
# Print first 5 rows 
print(df.head())

# Save to CSV File
df.to_csv('largest_us_companies.csv', index=False)



