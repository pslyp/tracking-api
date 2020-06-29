from fastapi import FastAPI
import os
from selenium import webdriver
import sys
import time
import urls

sys.path.insert(0, 'adapters/')

import package_code
import thaipost
import kerry
import flash
import response_template

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to track api."

@app.get("/api/v1.0/track/{barcode}")
def track(barcode: str):   

    company = package_code.company(barcode)
    if company == "thaipost":
        print("Thaipost")
        return thaipost.api(barcode)
    elif company == "flash":
        print("Flash")
        return flash.api(barcode)        
    elif company == "kerry":
        print("Kerry")
        return kerry.api(barcode)
    else:
        return response_template.success(422, "Unprocessable Entit", None)

@app.get("/test/{barcode}")
def test(barcode: str):
    bc = barcode + " "
    print(bc[0:2])
    print(bc[-3:-1])