from fastapi import FastAPI  
app = FastAPI(title="ODIA.dev Voice Engine")  
  
@app.get("/")  
def home():  
    return {"message": "???? ODIA.dev Voice Engine - Nigeria Ready!", "company": "ODIA.dev", "ceo": "Austyn Eguale", "status": "ACTIVE", "brand": "ODIA.dev"}  
  
@app.get("/health")  
def health():  
    return {"status": "ODIA.dev Voice Engine - 100%% Operational", "company": "ODIA.dev", "location": "Lagos Nigeria", "brand": "ODIA.dev"}  
  
@app.get("/speak")  
def speak(text="Hello Nigeria", agent="lexi"):  
    return {"message": f"ODIA.dev Voice: {text}", "agent": agent, "cost": "?1", "brand": "ODIA.dev", "status": "SUCCESS"}  
  
if __name__ == "__main__":  
    import uvicorn  
    print("?? ODIA.dev VOICE ENGINE STARTING...")  
    print("?? Brand: ODIA.dev")  
    print("????? CEO: Austyn Eguale")  
    print("???? Made in Nigeria")  
    print("?? Access: http://localhost:8001")  
    uvicorn.run(app, host="127.0.0.1", port=8001) 
