# How to Bypass Cloudflare in Python Using undetected_chromedriver Module

# pip install undetected-chromedriver

import undetected_chromedriver as uc 

driver = uc.Chrome() 
driver.get('https://opensea.io/rankings/trending')
