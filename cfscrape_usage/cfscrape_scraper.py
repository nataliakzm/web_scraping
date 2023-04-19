# A simple cfscrape scraper to scrape a Cloudflare-protected website

#pip install cfscrape

import cfscrape 
 
scraper = cfscrape.create_scraper() 
response = scraper.get('https://www.glassdoor.com/about') 
print(response.text) 
 
with open('./file.html', '+w') as file: 
	file.write(response.text)