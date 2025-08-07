from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS
import os
import time
import uuid

# Create your robot
app = FastAPI(title="Nigerian Voice Robot", version="1.0.0")

# Let other apps talk to your robot
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Create folder for voice files
os.makedirs("voices", exist_ok=True)

class VoiceRequest(BaseModel):
    text: str           
    agent: str = "lexi" 

# Your 4 Nigerian friends
NIGERIAN_FRIENDS = {
    "lexi": "Hello! I am Lexi, your friendly Nigerian business helper!",
    "miss": "Good day! I am Miss, your Nigerian university assistant!",
    "atlas": "Welcome! I am Atlas, your Nigerian travel expert!",
    "legal": "Greetings! I am Miss Legal, your Nigerian compliance helper!"
}

@app.get("/")
def home():
    return {
        "message": "Your Nigerian Voice Robot is ALIVE!",
        "friends": list(NIGERIAN_FRIENDS.keys()),
        "status": "Ready to speak Nigerian!"
    }

@app.post("/speak")
def make_nigerian_speak(request: VoiceRequest):
    try:
        print(f"Making Nigerian voice say: {request.text[:50]}...")
        
        # Create Nigerian voice with Nigerian accent
        tts = gTTS(
            text=request.text, 
            lang='en',           
            tld='com.ng',        # This gives Nigerian accent!
            slow=False
        )
        
        # Save the voice file
        filename = f"nigerian_voice_{uuid.uuid4().hex[:8]}.mp3"
        filepath = f"voices/{filename}"
        tts.save(filepath)
        
        return {
            "success": True,
            "message": "Nigerian voice created!",
            "voice_file": filename,
            "download_url": f"/download/{filename}",
            "agent": request.agent
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Voice creation failed: {str(e)}")

@app.get("/download/{filename}")
def download_voice(filename: str):
    filepath = f"voices/{filename}"
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Voice file not found")
    
    return FileResponse(filepath, media_type="audio/mpeg", filename=filename)

@app.get("/test")
def test_all_voices():
    results = {}
    
    for friend_name, greeting in NIGERIAN_FRIENDS.items():
        try:
            # Make voice for each friend
            tts = gTTS(text=greeting, lang='en', tld='com.ng', slow=False)
            filename = f"test_{friend_name}.mp3"
            filepath = f"voices/{filename}"
            tts.save(filepath)
            
            results[friend_name] = {
                "status": "success",
                "voice_file": filename,
                "download_url": f"/download/{filename}"
            }
            
        except Exception as e:
            results[friend_name] = {
                "status": "failed",
                "error": str(e)
            }
    
    return {
        "message": "Voice test complete!",
        "results": results
    }

if __name__ == "__main__":
    print("Starting Nigerian Voice Robot...")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)