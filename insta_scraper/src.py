#Step 1: Set up the environment

# pip install selenium (if you don't have it already)
# Download the latest version of chromedriver.exe from https://chromedriver.chromium.org/downloads


#Step 2: Log in to the Instagram account using Selenium

# Import the necessary packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Then, specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('path\to\chromedriver.exe')

# Open the IG homepage 
driver.get("http://www.instagram.com")

# Target the username & password fields and enter your credentials
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Enter your username and password (you can also use the Keys.RETURN to submit the form)
username.clear()
username.send_keys("your_username")
password.clear()
password.send_keys("your_password")


#Step 3: Handling pop-up messages and notifications

# At this point, we face the first challenge with a poping-up message to accept cookies (if you are in the EU)
cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Only allow essential cookies")]'))).click()

# We can finally target the login button and click it
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()

#We are logged in! 

#But, don't be too happy yet, as we still need to pass two more popping-up notifications (one for notifications and one for saving login info)
# Handle, the first one with this line of code:
popup1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# In case you have a second one, run this:
popup1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


#Step 4: Crawling Instagram Hashtags and Posts URLs using Selenium

# Import the necessary packages
import time

# Specify the search box here and clear it
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search.clear()

#FIRST METHOD: Search for the hashtag 
keyword = "#pets"
search.send_keys(keyword)

# Wait for 5 seconds 
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(5)
search.send_keys(Keys.ENTER)
time.sleep(5)

# Scroll down to the page bottom to load more posts (you can change the range to load more posts)
driver.execute_script("window.scrollTo(0, 4000);")

# Scrape all posts on the page and store them in a list called posts 
posts = driver.find_elements(By.TAG_NAME,'a')
posts = [a.get_attribute('href') for a in posts]

# Narrow down all links to image links only 
posts = [a for a in posts if str(a).startswith("https://www.instagram.com/p/")]

# Get rid of your avatar and IG’s logo from the results 
posts[:-2]


#SECOND METHOD: Scrape the elements tagged with the img attribute
images = []

# You can continue and extract directly image links from the posts 
for a in posts:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements(By.TAG_NAME,'img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])

images[:5]