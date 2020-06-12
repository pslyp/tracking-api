from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to track api."

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)