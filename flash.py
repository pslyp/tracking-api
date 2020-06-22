from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
import sys
import time
import urls

sys.path.insert(0, 'adapters/')

import template
import flash_adapter


def web(barcode):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    CHROMEDRIVER_PATH = 'D:\Python\chromedriver'
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    # browser.get(urls.FLASH_API + barcode)

    return { "status": 200, "message": "Not available", "data": None }

def api(barcode):
    res = requests.get(urls.FLASH_API + barcode)
    staCode = res.status_code

    if staCode == 200:
        js = res.json()
        api = flash_adapter.convert(js)
    elif staCode == 422:
        api = {
            "status": 204,
            "message": "Shipment not found!",
            "data": None
        }
    elif staCode == 404:
        api = {
            "status": 404,
            "message": "Path not found",
            "data": None
        }
    else:
        print("Flash Code:", staCode)

    return api