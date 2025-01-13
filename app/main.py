from fastapi import FastAPI, Depends, HTTPException, Header
from datetime import datetime
from typing import Optional
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
@app.get("/time")
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": now}
API_KEY = "mysecureapikey"

# Dependency xác thực API Key
def verify_api_key(api_key: Optional[str] = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/secure-data/", dependencies=[Depends(verify_api_key)])
def get_secure_data():
    return {"message": "You have access to secure data"}