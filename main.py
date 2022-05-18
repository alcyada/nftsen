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
import os                                                                 
app = FastAPI()                                                           
                                                                          
url = "https://api.nft.storage/upload"                                    
                                                                          
headers = CaseInsensitiveDict()                                           
headers["accept"] = "application/json"                                    
headers[                                                                  
    "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzd$
headers["Content-Type"] = "image/*"                                       
header = CaseInsensitiveDict()                                            
header["accept"] = "application/json"                                     
header[                                                                   
    "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzd$
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
                                                                          
@app.get("/nft/{query}")                                                  
async def read_item(query: str):                                          
    driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver",    
                            log_path='/home/ubuntu/geckodriver.log',      
                           options=opts)                                  
                                                                          
    driver.get("https://hotpot.ai/art-maker?s=nft-generator")             
    driver.find_element(By.CSS_SELECTOR, "textarea").click()              
    driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(query)
    driver.find_element(By.ID, "rootYield").click()                       
    driver.find_element(By.ID, "submitButton").click()                    
    # with open('n.png', 'wb') as file:                                   
    #    file.write(driver.get_full_page_screenshot_as_png())             
    is_available = False                                                  
    cnt = 10                                                              
    while(not is_available):                                              
        print("Image Processing start ...", flush=True)                   
        await asyncio.sleep(30 * 1)                                       
        # with open('n2.png', 'wb') as file:                              
        #     file.write(driver.get_full_page_screenshot_as_png())        
        try:                                                              
            driver.find_element(By.XPATH, '//*[@id="cookieOverlay"]/div[2$
        except Exception:                                                 
            pass                                                          
        try:                                                              
            el = driver.find_element(By.XPATH,                            
                             '//*[@id="resultListBox"]/div/div[1]/img')   
            m = el.get_attribute('src')                                   
                                                                          
            response = requests.get(m)                                    
            gif_len = len(response.content)                               
            print(f"{cnt} - {gif_len}", flush=True)                       
            if gif_len == 43:                                             
                raise Exception                                           
            file = open(f"{query}.png", "wb")                             
            file.write(response.content)                                  
            file.close()                                                  
                                                                          
                                                                          
            is_available = True                                           
        except Exception as ex:                                           
            print(f"LAST CNT : {cnt} - {ex}")                             
            if (cnt <= 0):                                                
                raise RuntimeError                                        
        cnt -= 1                                                          
    print(m)
    img = f"{query}.png"                                                  
    data = open(f"{query}.png", 'rb')                                     
    resp = requests.post(url, headers=headers, data=data)                 
    a = resp.json()                                                       
    print(a)                                                              
    itt = a["value"]["cid"]                                               
    print(itt)                                                            
    dit = {                                                               
        "name": f"{query} - A artpiece by aiverse",                       
        "description": "A piece of art made by an ai employed at aiverse.$
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
    os.remove(f"{query}.png")                                             
    os.remove(f"dit{query}.json")                                         
    hash = p["value"]["cid"]                                              
    print(hash)                                                           
    driver.close()                                                        
    return {"query": f"https://{hash}.ipfs.nftstorage.link/"}
