"""
Quotes Scraper - Python Script

This script scrapes quotes, authors, and tags from the website "https://quotes.toscrape.com/". 
It follows these steps:

1. Start from the homepage and iterate through paginated pages.
2. Extract:
   - Quotes
   - Authors
   - Tags associated with each quote.
3. Stop when no more quotes are found.
4. Store and print all **unique authors** in a formatted column layout.
"""

import requests
import bs4

# Base URL of the quotes website
BASE_URL = "https://quotes.toscrape.com/"

# Initialize variables
page = 1  # Start from page 1
unique_authors = set()

print("\nStarting web scraping...\n")

while True:
    # Construct the URL dynamically for pagination
    url = f"{BASE_URL}/page/{page}" if page > 1 else BASE_URL
    print(f"Scraping: {url}")

    # Send GET request
    result = requests.get(url)
    
    # Stop if no more quotes are found (end of pagination)
    if "No quotes found!" in result.text:
        print("\nNo more quotes found. Stopping...\n")
        break

    # Parse HTML using BeautifulSoup
    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    # Extract authors
    authors = {author.text.strip() for author in soup.select(".author")}
    
    # Extract quotes
    quotes = [quote.text.strip() for quote in soup.select('.text')]
    
    # Extract tags
    tags = {tag.text for tag in soup.select('.tags .tag')}

    # Print scraped quotes
    print("\n".join(quotes))
    
    # Print extracted tags
    print(f"\nTags: {', '.join(tags)}\n")

    # Store unique authors
    unique_authors.update(authors)

    # Move to the next page
    page += 1

# Format and print unique authors in columns
print("\nUnique Authors:\n" + "-" * 40)

# Sort authors alphabetically
unique_authors_sorted = sorted(unique_authors)
columns = 2  # Number of columns per row

for i in range(0, len(unique_authors_sorted), columns):
    row = [f"{i + j + 1}) {unique_authors_sorted[i + j]:<20}" for j in range(columns) if i + j < len(unique_authors_sorted)]
    print(" ".join(row))

print("\nScraping completed successfully! ✅")
