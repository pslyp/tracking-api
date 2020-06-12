from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
import urls

def getApi(barcode: str):
    result = search(barcode)

    return result

def search(barcode: str):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.binary_location = GOOGLE_CHROME_BIN

    browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    browser.get(urls.KERRY + barcode)
    page_source = browser.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    trackInput = soup.find("input", {"class":"iCode"})
    trackBtn = soup.find("input", {"class":"btn", "value":"ติดตาม"})
    btnId = trackBtn["id"]

    print("ID: ", trackBtn["id"])

    btn = browser.find_element_by_id(btnId)
    btn.click()

    time.sleep(1)

    print(browser.current_url)

    source = browser.page_source
    print(source)

    soup = ""
    soup = BeautifulSoup(source, 'lxml')

    print(soup.prettify)

    info = soup.find("div", {"class":"info"})
    spans = info.find_all("span")  

    span = list(spans)

    barcode = span[0].string
    etd = span[1].string
    sender = span[3].string
    receiver = span[4].string

    for span in list(spans):    
        print(span.string)

    statusCols = soup.find("div", {"class":"colStatus"})

    statusJsonArr = []
    statusRows = statusCols.children

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
            
            statusJson = { "code": code,
                        "date": dtStr,
                        "detail": detail,
                        "province": province }
            
            statusJsonArr.append(statusJson)
            
    x = {
        "info": {
            "barcode": barcode,
            "expected_to_date": etd,
            "sender": sender,
            "receiver": receiver
        },
        "status": statusJsonArr
    }

    return x