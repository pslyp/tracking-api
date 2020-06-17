from fastapi import FastAPI
import os
from selenium import webdriver
import time
import urls

import thaipost
import kerry

# EH535515481TH

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to track api."

@app.get("/api/v1.0/track/{barcode}")
def track(barcode: str):
    res = {}
    bc = barcode + " "
    if bc[-3:-1] == "TH":
        res = thaipost.api(barcode)
    else:
        res = kerry.api(barcode)

    return res

@app.get("/test/{barcode}")
def test(barcode: str):
    bc = barcode + " "
    print(bc[0:2])
    print(bc[-3:-1])