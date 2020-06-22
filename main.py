from fastapi import FastAPI
import os
from selenium import webdriver
import time
import urls

import thaipost
import kerry
import flash

# EH535515481TH

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to track api."

@app.get("/api/v1.0/track/{barcode}")
def track(barcode: str):
    res = {}

    asciiCode = 0 
    for b in barcode[0:2]: asciiCode+=ord(b)
    firstTwoPos = barcode[0:2]
    lastTwoPos = (barcode+" ")[-3:-1]

    seven = barcode[6]

    # print(firstTwoPos)
    # print(seven)

    if lastTwoPos == "TH":
        res = thaipost.api(barcode)
        print("Thaipost")   
    elif firstTwoPos == "TH":
        res = flash.api(barcode)
        print("Flash")
    elif (asciiCode >= 130 and asciiCode <= 180):
        res = kerry.api(barcode)
        print("Kerry")

    return res

@app.get("/test/{barcode}")
def test(barcode: str):
    bc = barcode + " "
    print(bc[0:2])
    print(bc[-3:-1])