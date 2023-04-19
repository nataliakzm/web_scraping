# Combining cfscrape with Other Libraries to crawl a Cloudflare-protected website

#pip install cfscrape
#pip install BeautifulSoup

import cfscrape 
from bs4 import BeautifulSoup 
 
scraper = cfscrape.create_scraper() 
response = scraper.get('https://www.glassdoor.com/about') 
soup = BeautifulSoup(response.text, 'html.parser') 
 
# To return src attribute of all images on the page 
for img in soup.find_all('img'): 
	print(img.get('src'))