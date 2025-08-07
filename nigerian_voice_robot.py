#!/usr/bin/env python3
"""
🇳🇬 NIGERIAN VOICE ROBOT - FRESH CODE
No debugging, no bullshit, just works.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import time
import uuid

# Install these if missing
try:
    from gtts import gTTS
except ImportError:
    print("❌ Installing gtts...")
    os.system("pip install gtts")
    from gtts import gTTS

# Create the robot
app = FastAPI(title="🇳🇬 Nigerian Voice Robot", version="1.0")

# Allow web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create voice folder
os.makedirs("voices", exist_ok=True)

class VoiceRequest(BaseModel):
    text: str
    agent: str = "lexi"

# Nigerian agents
AGENTS = {
    "lexi": "Hello! I am Agent Lexi from ODIA Nigeria! I help businesses grow!",
    "miss": "Good day! I am Agent MISS, your Nigerian university assistant!",
    "atlas": "Welcome! I am Agent Atlas, your luxury Nigerian travel expert!",
    "legal": "I am Agent Miss Legal, your Nigerian compliance specialist!"
}

@app.get("/")
def home():
    return {
        "message": "🇳🇬 Nigerian Voice Robot is ALIVE!",
        "status": "ready",
        "agents": list(AGENTS.keys())
    }

@app.post("/speak")
def create_nigerian_voice(request: VoiceRequest):
    """Create Nigerian voice - NO BULLSHIT"""
    try:
        print(f"🎙️ Creating Nigerian voice: {request.text[:50]}...")
        
        # Create Nigerian voice
        tts = gTTS(
            text=request.text,
            lang='en',
            tld='com.ng',  # Nigerian accent
            slow=False
        )
        
        # Save voice file
        filename = f"nigerian_{request.agent}_{uuid.uuid4().hex[:8]}.mp3"
        filepath = f"voices/{filename}"
        tts.save(filepath)
        
        print(f"✅ Voice created: {filename}")
        
        return {
            "success": True,
            "message": f"Nigerian {request.agent} voice ready!",
            "voice_file": filename,
            "download_url": f"/download/{filename}",
            "agent": request.agent
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=f"Voice failed: {str(e)}")

@app.get("/download/{filename}")
def download_voice(filename: str):
    """Download voice file"""
    filepath = f"voices/{filename}"
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Voice not found")
    return FileResponse(filepath, media_type="audio/mpeg")

@app.get("/test")
def test_all_agents():
    """Test all Nigerian agents"""
    results = {}
    
    for agent, greeting in AGENTS.items():
        try:
            tts = gTTS(text=greeting, lang='en', tld='com.ng', slow=False)
            filename = f"test_{agent}.mp3"
            filepath = f"voices/{filename}"
            tts.save(filepath)
            
            results[agent] = {
                "status": "✅ SUCCESS",
                "voice_file": filename,
                "download_url": f"/download/{filename}"
            }
            print(f"✅ {agent}: Voice created")
            
        except Exception as e:
            results[agent] = {"status": "❌ FAILED", "error": str(e)}
            print(f"❌ {agent}: {e}")
    
    return {
        "message": "🧪 Voice test complete!",
        "results": results
    }

if __name__ == "__main__":
    print("🚀 STARTING NIGERIAN VOICE ROBOT...")
    print("🇳🇬 Ready to create authentic Nigerian voices!")
    
    try:
        import uvicorn
    except ImportError:
        print("📥 Installing uvicorn...")
        os.system("pip install uvicorn")
        import uvicorn
    
    # Start the robot
    uvicorn.run(app, host="0.0.0.0", port=8001)