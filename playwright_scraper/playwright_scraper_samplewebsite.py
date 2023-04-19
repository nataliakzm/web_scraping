# How to Use Playwright for Web Scraping 

# Step 1: Locate Elements and Extract Text Content 

# Import libraries to deploy into scraper 
import asyncio 
from playwright.async_api import Playwright, async_playwright 
 
# Start with playwright scraping here:  
async def scrape_data(page): 
	scraped_elements = [] 
	items = await page.query_selector_all("li.product") 
 
	# Pick the scraping item from the list of items 
	for i in items: 
		scraped_element = {} 
 
		# Product name  
		el_title = await i.query_selector("h2") 
		scraped_element["product"] = await el_title.inner_text() 
 
		# Product price  
		el_price = await i.query_selector("span.woocommerce-Price-amount") 
		scraped_element["price"] = await el_price.text_content() 
 
		scraped_elements.append(scraped_element) 
	return scraped_elements 
 
 
async def run(playwright: Playwright) -> None: 
	
	# Launch the headed browser instance (headless=False)  
	# To see the process of playwright scraping 
	# chromium.launch - opens a Chromium browser instance 

	browser = await playwright.chromium.launch(headless=False) 
 
	# Creates a new browser context  
	context = await browser.new_context() 
 
	# Open new page in the context  
	page = await context.new_page() 
 
	# Go to the chosen website  
	await page.goto("https://scrapeme.live/shop/") 
	data = await scrape_data(page) 
 
	print(data) 
 
	await context.close() 
	
	# Turn off the browser once you finished  
	await browser.close() 
 
 
async def main() -> None: 
	async with async_playwright() as playwright: 
		await run(playwright) 
 
asyncio.run(main())