import requests
from bs4 import BeautifulSoup
import csv

# Initialization
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 37
page_size = 100
Reviews = []

# Scraping through pages
for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        Reviews.append(para.get_text())

    print(f"   ---> {len(Reviews)} total Reviews")

# Store data in a CSV file
csv_file = 'reviews_data.csv'

# Open a CSV file for writing with 'utf-8' encoding
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write a header row
    writer.writerow(['Reviews'])

    # Write the data from the 'Reviews' list to the CSV file
    for review in Reviews:
        writer.writerow([review])

print(f'{len(Reviews)} reviews have been written to {csv_file}')
