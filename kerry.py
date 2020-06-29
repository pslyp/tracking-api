from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
import sys
import time
import urls

sys.path.insert(0, 'adapters/')

import kerry_adapter
import json_template
import response_template


def web(barcode):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    # CHROMEDRIVER_PATH = 'D:\Python\chromedriver'
    # browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get(urls.KERRY_WEB+barcode)

    time.sleep(8)

    button = browser.find_element_by_css_selector('input.btn')
    button.click()

    time.sleep(2)

    page_source = browser.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    # Info
    info = soup.find("div", {"class":"info"})
    spans = info.find_all("span")  

    span = list(spans)

    barcode = span[0].string
    etd = span[1].string
    sender = span[3].string
    receiver = span[4].string

    infoArr = [ barcode, etd, sender, receiver ]

    # Status
    statusCols = soup.find("div", {"class":"colStatus"})

    # statusJsonArr = []
    statusRows = statusCols.children

    statusArr = []
    s=False
    for row in statusRows:
        if len(row) > 1:
            code = 0

    #       ดึงค่า status
            status = row["class"][1].split("-")[1]
            if status == "success":
                code = 200
                s=True
            else:
                code = 300
                s=False
            
    #       ดึงค่า date&time
            r=1
            dtStr = ""
            dateTime = row.find("div", {"class":"date"})
            for dt in dateTime.children:
                dtLen = len(dt.string)            
                if dtLen > 1:
                    if r == 2:
                        dtStr += " "
                    dtStr += dt.string[5:dtLen]
                    r+=1

    #       ดึงค่า detail
            desc = row.find("div", {"class":"desc"})
            descList = list(desc.children)
            detail = descList[1].text.strip()
            if s: detail = detail[0:detail.index(" ")].strip()  
            province = descList[3].text.strip()
            
    #         statusJson = '{ "code": "'+str(code)+'", '
    #         statusJson +=  '"date": '+('"'+dtStr+'"')+', '
    #         statusJson +=  '"detail": '+('"'+detail+'"')+', '
    #         statusJson +=  '"province": '+('"'+province+'"')+' }'
            
            # statusJson = { "code": code,
            #             "date": dtStr,
            #             "detail": detail,
            #             "province": province }
            
            # statusJsonArr.append(statusJson)

            statusRow = [ code, dtStr, detail, province ]
            statusArr.append(statusRow)

    # x = {
    #     "info": {
    #         "barcode": barcode,
    #         "expected_to_date": etd,
    #         "sender": sender,
    #         "receiver": receiver
    #     },
    #     "status": statusJsonArr
    # }

    # print(statusArr)            

    browser.close()
    browser.quit()

    return json_template.json(infoArr, statusArr)

def api(barcode):
    res = requests.get(urls.KERRY_API + barcode + '/th')
    staCode = res.status_code

    if staCode == 200:
        js = res.json()
        err = list(js.keys())[0]  

        if err == "error":
            print("[Kerry]: Api error >>", js["error"]["code"]) 
            api = web(barcode)
        else: 
            api = kerry_adapter.convert(js)

    elif staCode == 404:
        api = response_template.success(204, "Shipment not found!", None)
    
    else:
        api = response_template.error(500, "Internal Server Error")

    return api