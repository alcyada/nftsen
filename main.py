from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(service=Service("/usr/bin/geckodriver"), options=opts)
driver.get("https://hotpot.ai/art-maker?s=nft-generator")
driver.get("https://hotpot.ai/art-maker?s=nft-generator")
driver.find_element(By.CSS_SELECTOR, "textarea").click()
driver.find_element(By.CSS_SELECTOR, "textarea").send_keys("sunrise")
driver.find_element(By.ID, "rootYield").click()
driver.find_element(By.ID, "submitButton").click()
with open('n.png', 'wb') as file:
 file.write(driver.get_full_page_screenshot_as_png())
sleep(30)
with open('n2.png', 'wb') as file:
 file.write(driver.get_full_page_screenshot_as_png())
driver.find_element(By.XPATH, '//*[@id="cookieOverlay"]/div[2]').click()
el=driver.find_element(By.XPATH, '//*[@id="resultListBox"]/div/div[1]/img')
m= el.get_attribute('src')
print(m)
response = requests.get(m)

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()
