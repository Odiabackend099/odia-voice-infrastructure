# 🇳🇬 SUPER SIMPLE NIGERIAN TTS WEB API
# Copy this file and save it as "main.py"

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import time
from gtts import gTTS
from supabase import create_client, Client
import asyncio

# Your existing Supabase credentials (already working!)
SUPABASE_URL = "https://qgqfiluokypqmloknxlh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFncWZpbHVva3lwcW1sb2tueGxoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzU1MTEwNSwiZXhwIjoyMDY5MTI3MTA1fQ.hhRpm-21UrSIQeGU-_TPNXNvDT6TPem1tz-67R2ro_o"

# Create the web app
app = FastAPI(title="🇳🇬 ODIA Nigerian TTS API", version="1.0.0")

# Allow your Lovable app to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your actual domain
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Connect to your database
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create output folder for audio files
os.makedirs("audio_files", exist_ok=True)

class TTSRequest(BaseModel):
    """What people need to send to get voice"""
    text: str          # What to say
    agent: str         # Which Nigerian friend should say it
    language: str = "en"  # What language (English by default)

# Your 4 Nigerian AI friends
NIGERIAN_AGENTS = {
    "lexi": {
        "name": "Agent Lexi",
        "personality": "Friendly WhatsApp helper",
        "voice_style": "excited and helpful",
        "greeting": "Hello! I'm Lexi and I'm so excited to help your business!"
    },
    "miss": {
        "name": "Agent MISS", 
        "personality": "University teacher",
        "voice_style": "professional and smart",
        "greeting": "Good day! I am Agent MISS, your academic assistant."
    },
    "atlas": {
        "name": "Agent Atlas",
        "personality": "Luxury travel expert", 
        "voice_style": "calm and sophisticated",
        "greeting": "Welcome! I'm Atlas, your premium experience specialist."
    },
    "legal": {
        "name": "Agent Miss Legal",
        "personality": "Legal compliance expert",
        "voice_style": "serious and precise", 
        "greeting": "I am Miss Legal, your Nigerian compliance specialist."
    }
}

def create_nigerian_voice(text: str, agent: str) -> str:
    """
    This is where the magic happens!
    Takes text and agent name, returns audio file path
    """
    print(f"🎙️ Creating {agent} voice saying: '{text[:50]}...'")
    
    # Make the text sound more Nigerian based on the agent
    if agent == "lexi":
        # Lexi is excited and friendly
        if not any(word in text.lower() for word in ["!", "excited", "amazing"]):
            text = f"Hello! {text} I'm so excited to help you!"
    
    elif agent == "miss":
        # MISS is professional and academic
        if not text.startswith(("Good", "Welcome", "Today")):
            text = f"Good day! {text} Thank you for learning with us."
    
    elif agent == "atlas": 
        # Atlas is calm and sophisticated
        text = f"Welcome! {text} We look forward to serving you."
    
    elif agent == "legal":
        # Legal is serious and precise
        text = f"Please note: {text} Ensure compliance with all regulations."
    
    try:
        # Create the voice using Google TTS with Nigerian accent
        # The 'com.ng' makes it sound more Nigerian!
        tts = gTTS(text=text, lang='en', tld='com.ng', slow=False)
        
        # Create unique filename
        filename = f"nigerian_{agent}_{int(time.time())}.mp3"
        filepath = f"audio_files/{filename}"
        
        # Save the audio file
        tts.save(filepath)
        
        print(f"✅ Voice created: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Voice creation failed: {e}")
        raise HTTPException(status_code=500, detail="Could not create voice")

@app.get("/")
async def home():
    """Home page - shows that your API is working"""
    return {
        "message": "🇳🇬 ODIA Nigerian TTS API is running!",
        "agents": list(NIGERIAN_AGENTS.keys()),
        "usage": "POST to /create-voice with {text, agent, language}",
        "status": "Ready to make Nigerian voices!"
    }

@app.get("/agents")
async def list_agents():
    """Show all your Nigerian AI friends"""
    return {
        "agents": NIGERIAN_AGENTS,
        "total": len(NIGERIAN_AGENTS),
        "message": "These are your Nigerian AI voice agents!"
    }

@app.post("/create-voice")
async def create_voice(request: TTSRequest):
    """
    This is the main endpoint - creates Nigerian voices!
    
    Send: {"text": "Hello Nigeria!", "agent": "lexi", "language": "en"}
    Get back: Audio file URL
    """
    
    # Check if agent exists
    if request.agent not in NIGERIAN_AGENTS:
        raise HTTPException(
            status_code=400, 
            detail=f"Agent '{request.agent}' not found. Use: {list(NIGERIAN_AGENTS.keys())}"
        )
    
    # Check text length
    if len(request.text) > 1000:
        raise HTTPException(status_code=400, detail="Text too long! Keep it under 1000 characters.")
    
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Please provide some text to speak!")
    
    try:
        # Create the voice file
        audio_file = create_nigerian_voice(request.text, request.agent)
        
        # Log to your Supabase database
        log_data = {
            "agent": request.agent,
            "text": request.text[:200],  # First 200 characters
            "audio_file": audio_file,
            "created_at": time.strftime('%Y-%m-%d %H:%M:%S'),
            "status": "success"
        }
        
        try:
            supabase.table('odia_tts_logs').insert(log_data).execute()
            print("✅ Logged to Supabase!")
        except:
            print("⚠️ Supabase logging failed, but voice still created")
        
        # Return success response
        return {
            "success": True,
            "message": f"{NIGERIAN_AGENTS[request.agent]['name']} is ready!",
            "agent": request.agent,
            "audio_file": audio_file,
            "download_url": f"/download/{audio_file.split('/')[-1]}",
            "text_spoken": request.text
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{filename}")
async def download_audio(filename: str):
    """Download the audio file"""
    file_path = f"audio_files/{filename}"
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
    
    return FileResponse(
        path=file_path,
        media_type='audio/mpeg',
        filename=filename
    )

@app.get("/test-voices")
async def test_all_voices():
    """Test all 4 agents - good for checking everything works"""
    test_results = {}
    
    for agent_id, agent_info in NIGERIAN_AGENTS.items():
        try:
            # Create a test voice for each agent
            test_text = agent_info["greeting"]
            audio_file = create_nigerian_voice(test_text, agent_id)
            
            test_results[agent_id] = {
                "status": "success",
                "audio_file": audio_file,
                "download_url": f"/download/{audio_file.split('/')[-1]}",
                "message": f"{agent_info['name']} voice created!"
            }
            
        except Exception as e:
            test_results[agent_id] = {
                "status": "failed", 
                "error": str(e),
                "message": f"{agent_info['name']} voice failed"
            }
    
    return {
        "message": "🧪 Voice test complete!",
        "results": test_results,
        "instruction": "Play the audio files to hear your Nigerian agents!"
    }

if __name__ == "__main__":
    print("🚀 Starting ODIA Nigerian TTS API...")
    print("🇳🇬 Ready to create authentic Nigerian voices!")
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)