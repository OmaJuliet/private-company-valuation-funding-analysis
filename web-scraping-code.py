import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = "https://finance.yahoo.com/markets/private-companies/highest-valuation/?start=0&count=150"
headers = {'User-Agent': 'Mozilla/5.0'}

# Send HTTP request
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the table (Inspect the webpage to find the correct class)
table = soup.find('table')  # Modify if there's a specific class

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip header row
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Store in a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Display the DataFrame
print(df)

# Save to CSV (optional)
df.to_csv("private_companies_highest_valuation.csv", index=False)
