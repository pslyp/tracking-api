from fastapi import FastAPI
import kerryWEB
import kerryAPI

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to track api."

@app.get("/api/v1.0/track/{barcode}")
def track(barcode: str): 
    return kerryWEB.getApi(barcode) 