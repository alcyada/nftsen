import asyncio
import json

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

app = FastAPI()

url = "https://api.nft.storage/upload"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers[
    "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweERDMjBCQmZmODI1YzgzMzY3ZjlBODc5MmU3NTA4ODE3OTE1NjQ5RjciLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1MjAzNzg2MzY5NiwibmFtZSI6ImFpdmVyc2UifQ.UAmNR8bj6RES1BqMW5v-W1u-rKLoZ6xWMsqzQ9yL3zo"
headers["Content-Type"] = "image/*"
header = CaseInsensitiveDict()
header["accept"] = "application/json"
header[
    "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweERDMjBCQmZmODI1YzgzMzY3ZjlBODc5MmU3NTA4ODE3OTE1NjQ5RjciLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1MjAzNzg2MzY5NiwibmFtZSI6ImFpdmVyc2UifQ.UAmNR8bj6RES1BqMW5v-W1u-rKLoZ6xWMsqzQ9yL3zo"
header["Content-Type"] = "json/*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
projectId = "28FNT2SlVaxu2dZrgAYolOkhXNX"
projectSecret = "5847d2bf588a435ef262228c0bd2321a"
endpoint = "https://ipfs.infura.io:5001"
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(service=Service("/usr/bin/geckodriver"),
                           options=opts)


@app.get("/nft/{query}")
async def read_item(query: str):
    driver.get("https://hotpot.ai/art-maker?s=nft-generator")
    driver.find_element(By.CSS_SELECTOR, "textarea").click()
    driver.find_element(By.CSS_SELECTOR, "textarea").send_keys("sunrise")
    driver.find_element(By.ID, "rootYield").click()
    driver.find_element(By.ID, "submitButton").click()
    with open('n.png', 'wb') as file:
        file.write(driver.get_full_page_screenshot_as_png())

    await asyncio.sleep(60 * 1)

    with open('n2.png', 'wb') as file:
        file.write(driver.get_full_page_screenshot_as_png())

    driver.find_element(By.XPATH, '//*[@id="cookieOverlay"]/div[2]').click()
    el = driver.find_element(By.XPATH,
                             '//*[@id="resultListBox"]/div/div[1]/img')
    m = el.get_attribute('src')
    print(m)
    response = requests.get(m)

    file = open(f"{query}.png", "wb")
    file.write(response.content)
    file.close()

    img = f"{query}.png"
    data = open(f"{query}.png", 'rb')
    resp = requests.post(url, headers=headers, data=data)
    a = resp.json()
    print(a)
    itt = a["value"]["cid"]
    print(itt)
    dit = {
        "name": f"{query} - A artpiece by aiverse",
        "description": "A piece of art made by an ai employed at aiverse. Aiverse is a deep-tech marketplace and no-code editors for making ai and metaverse",
        "image": f"https://{itt}.ipfs.nftstorage.link/",
        "linktree": "https://linktr.ee/aiversedai"
    }
    print(resp.status_code)
    with open(f'dit{query}.json', 'w', encoding='utf-8') as f:
        json.dump(dit, f, ensure_ascii=False, indent=4)
    data = open(f"dit{query}.json", 'rb')
    resp = requests.post(url, headers=header, data=data)
    p = resp.json()
    print(p)
    hash = p["value"]["cid"]
    print(hash)
    return {"query": f"https://{hash}.ipfs.nftstorage.link/"}
