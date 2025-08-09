# ODIA Voice Engine - Windows Ready 
from fastapi import FastAPI, Response 
import hashlib, json 
from datetime import datetime 
 
app = FastAPI(title="ODIA Voice Engine") 
odia_cache = {} 
daily_requests = 0 
 
@app.get("/") 
async def home(): 
    return {"message": "ODIA Voice Engine Running!", "status": "Active"} 
 
@app.get("/health") 
async def health(): 
    return {"status": "ODIA Voice Engine - Operational", "company": "ODIA AI LTD"} 
 
@app.get("/speak") 
async def speak(text: str = "Hello", agent: str = "lexi"): 
    return {"message": f"ODIA Voice: {text}", "agent": agent, "status": "Generated"} 
 
if __name__ == "__main__": 
    import uvicorn 
    print("?? ODIA VOICE ENGINE STARTING...") 
    uvicorn.run(app, host="0.0.0.0", port=8000) 
