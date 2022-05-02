from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(service=Service("/usr/bin/geckodriver"), options=opts)
driver.get("https://hotpot.ai/art-maker?s=nft-generator")
ids = driver.find_element_by_tag_name('textarea')
ids.click
ids.send_keys("some text")
ele=driver.find_element_by_tag_name('span')
ele.click
sleep(120)
ele2 = driver.find_element_by_class_name('imageBox.targetBox')
ele2.click
sleep(20)
ele3 = driver.find_element_by_tag_name('img')
ele3.click
file.write(el3.screenshot_as_png)