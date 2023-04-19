# How to Bypass Cloudflare in Python Using cfscrape

# pip install cfscrape

import cfscrape 
 
scraper = cfscrape.create_scraper() 
scraped_data = scraper.get('https://opensea.io/rankings/trending') 
print(scraped_data.text)
