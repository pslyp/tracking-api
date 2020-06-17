from fastapi import FastAPI
import os
from selenium import webdriver
import time
import urls

import kerryWEB
import kerryAPI

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to track api."

@app.get("/api/v1.0/track/{barcode}")
def track(barcode: str):
    res = kerryWEB.getApi(barcode)
    return res