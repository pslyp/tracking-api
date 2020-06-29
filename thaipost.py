from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
import sys
import time
import urllib3
import urls

urllib3.disable_warnings()

sys.path.insert(0, 'adapters/')

import thaipost_adapter
import json_template
import response_template


def web(barcode):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    # CHROMEDRIVER_PATH = "D:\Python\chromedriver"
    # browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get(urls.KERRY_WEB+barcode)

    return "Thaipost Web"

def api(barcode):

    payload = {
        'status': 'all',
        'language': 'TH',
        'barcode': [
            barcode
        ]
    }

    headers = {
        'Authorization': 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJzZWN1cmUtYXBpIiwiYXVkIjoic2VjdXJlLWFwcCIsInN1YiI6IkF1dGhvcml6YXRpb24iLCJleHAiOjE1OTQ1MTk4NjMsInJvbCI6WyJST0xFX1VTRVIiXSwiZCpzaWciOnsicCI6InpXNzB4IiwicyI6bnVsbCwidSI6IjI2MGQ2NzNhMjE3MTRmZDIyZTcyNzUxZDI4ZDU2YzM1IiwiZiI6InhzeiM5In19.2-pDB10a9l5V-WedP-bUxSZvtwj3nvxdsKVq6zLkRI9gvW2212ukZ0vSNBTcdtKxBhVAaf8X0m-pdtt1K78gWA',
        'Content-Type': 'application/json'
    }

    # res = requests.post(urls.THAIPOST_API, json=payload, headers=headers, verify=False)
    # staCode = res.status_code

    res = requests.get(urls.THAIPOST_API_2 + barcode)   
    staCode = res.status_code
    
    if staCode == 200:
        js = res.json()

        if js["status"] == 1:
            api = thaipost_adapter.convert(js)

    elif staCode == 500:
        js = res.json()

        if js["status"] == 0 and js["message"] == "Empty data.":
            api = response_template.success(204, "Shipment not found!", None)

    else:        
        api = response_template.error(500, "Internal Server Error")

    return api