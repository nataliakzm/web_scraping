# How to Bypass Cloudflare in Python Using cloudscraper Module

# pip install cloudscraper
# pip install bs4

import cloudscraper 
from bs4 import BeautifulSoup as bs 
 
scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 
content = scraper.get("https://opensea.io/rankings/trending").text 
 
print(content)

# To further process extracted data 
processed_content = bs(content, "html.parser") 

# These classes are not reliable, added here for demo purposes 
processed_content = processed_content.find_all(".eqFKWH .hmMxZB .mGAUR") 
 
scraped_data = list() 
for data in soup: 
	scraped_data.append(data.get_text()) 
 
print(scraped_data)