# A simple requests scraper to scrape a Cloudflare-protected website

#pip install requests

import requests 
scraper = requests.get('https://www.glassdoor.com') 
print(scraper.text)