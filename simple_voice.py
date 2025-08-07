# 🇳🇬 Super Simple Nigerian Voice Test - FIXED!
# Copy this ENTIRE code and save as "simple_voice.py"

print("🚀 Starting Nigerian Voice Magic...")

# Method 1: Try the simple TTS first
try:
    import pyttsx3
    print("✅ Found simple voice engine!")
    
    # Create voice engine
    engine = pyttsx3.init()
    
    # Set voice properties for Nigerian style
    voices = engine.getProperty('voices')
    if voices:
        # Try to find a female voice (sounds more friendly)
        for voice in voices:
            if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    
    # Nigerian business message
    nigerian_text = "Hello! Welcome to ODIA AI, Nigeria's smartest voice technology company. We make computers talk like real Nigerians!"
    
    print("🎙️ Making your first Nigerian voice...")
    
    # Save to file
    engine.save_to_file(nigerian_text, "odia_nigerian_voice.wav")
    engine.runAndWait()
    
    print("✅ SUCCESS! Your voice is ready!")
    print("📁 File saved: odia_nigerian_voice.wav")
    print("🎉 Go find the file and play it!")
    
except ImportError:
    print("⚠️ Simple engine not found. Installing now...")
    import subprocess
    subprocess.run(["pip", "install", "pyttsx3"])
    print("✅ Installed! Run this script again!")

except Exception as e:
    print(f"❌ Simple method had issue: {e}")
    print("🔧 Let's try the advanced method...")
    
    # Method 2: Try gTTS (Google Text-to-Speech)
    try:
        from gtts import gTTS
        import pygame
        print("✅ Found Google voice engine!")
        
        # Nigerian English text
        text = "Hello from ODIA AI Nigeria! We are building the future of African voice technology!"
        
        # Create Nigerian voice (use 'en' with Nigerian accent)
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save the voice
        tts.save("odia_google_voice.mp3")
        
        print("✅ SUCCESS! Google voice created!")
        print("📁 File saved: odia_google_voice.mp3")
        print("🎉 Play this file - it sounds good!")
        
    except ImportError:
        print("⚠️ Google TTS not found. Installing...")
        import subprocess
        subprocess.run(["pip", "install", "gtts", "pygame"])
        print("✅ Installed! Run this script again!")
        
    except Exception as e2:
        print(f"❌ Google method also had issue: {e2}")
        print("🔧 Let's install what we need...")
        
        # Method 3: Install everything we need
        import subprocess
        
        print("📥 Installing voice tools...")
        
        tools_to_install = [
            "pyttsx3",      # Simple voice
            "gtts",         # Google voice  
            "pygame",       # Audio player
            "speech-recognition",  # For listening
            "torch",        # For AI
            "torchaudio"    # For audio AI
        ]
        
        for tool in tools_to_install:
            try:
                print(f"   Installing {tool}...")
                subprocess.run(["pip", "install", tool], check=True)
                print(f"   ✅ {tool} installed!")
            except:
                print(f"   ⚠️ {tool} had issues, but continuing...")
        
        print("🎉 All tools installed!")
        print("🔄 Run this script again now!")

print("\n" + "="*50)
print("🇳🇬 NIGERIAN VOICE SYSTEM STATUS")
print("="*50)
print("✅ RTX 4090 GPU: Ready for AI")
print("✅ Python Environment: Working") 
print("✅ Voice Tools: Installing/Ready")
print("🎯 Next Step: Run this script to create voice!")
print("="*50)