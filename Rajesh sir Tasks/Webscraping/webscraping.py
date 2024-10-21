"""Web scraping:
Web-scraping is the process of extracting data from websites by accessing the HTML of a page and 
gathering specific information. In Python, popular libraries for web scraping include 
BeautifulSoup, requests, and Scrapy.
Here’s a simple example using BeautifulSoup and requests:"""
# Install required packages if you don't have them
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = "https://en.wikipedia.org/wiki/Puneeth_Rajkumar"
response = requests.get(url)

# Step 2: Parse the page's content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract the data you need (e.g., title of the page)
page_title = soup.title.string
print(f"Page title: {page_title}")

# Example to find all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
    
"""In this example:
We send a request to the website.
Parse the HTML content of the page.
Extract specific elements like the title and all the links (<a> tags). """
