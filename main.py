from fastapi import FastAPI

if __name__ == '__main__':
    import uvicorn
    uvicorn.run()

app = FastAPI()

@app.get('/')
def root():
    return "Welcome to track api."