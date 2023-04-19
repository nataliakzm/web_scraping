# How to Use Playwright for Web Scraping 

# Taking Screenshots with Playwright

from playwright.sync_api import sync_playwright 
 
with sync_playwright() as p: 
	browser = p.chromium.launch() 
	page = browser.new_page() 
	page.goto("https://www.amazon.com/dp/B00B7NPRY8/") 
 
	# Create a dictionary with the scraped data 
	item = { 
		"item_title": page.query_selector("#productTitle").inner_text(), 
		"author": page.query_selector(".contributorNameID").inner_text(), 
		"price": page.query_selector(".a-size-base.a-color-price.a-color-price").inner_text(), 
	} 
 
	print(item) 
 
	page.screenshot(path="item.png") 
	browser.close()