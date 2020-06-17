from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time
import urls


def web(barcode):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    CHROMEDRIVER_PATH = "D:\Python\chromedriver"
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    # browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get(urls.KERRY_WEB+barcode)

    return "Thaipost Web"

def restAPI(barcode):
    return { "status": 200, "data": None }

def api(barcode):
    return restAPI(barcode)