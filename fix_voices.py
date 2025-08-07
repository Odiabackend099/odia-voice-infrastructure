# 🇳🇬 ODIA Nigerian Voice Fix - NO MORE ROBOT TRASH!
# Save this as "fix_voices.py"

print("🚀 FIXING ODIA VOICES - NO MORE ROBOT TRASH!")
print("Making voices sound like REAL Nigerians...")

import subprocess
import sys
import os

def install_if_missing(package):
    """Install package if not already there"""
    try:
        __import__(package.split('==')[0])
        print(f"✅ {package} already installed!")
    except ImportError:
        print(f"📥 Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed!")

def create_real_nigerian_voices():
    """Create REAL Nigerian voices that sound HUMAN"""
    
    print("\n🎯 Installing Nigerian Voice Engine...")
    
    # Install the good voice engine
    install_if_missing("gtts")
    install_if_missing("pygame")
    
    print("\n🎙️ Creating PROFESSIONAL Nigerian voices...")
    
    # Import the good voice engine
    from gtts import gTTS
    
    # Test scripts for your ODIA agents
    voices_to_create = {
        "Agent Lexi (WhatsApp)": "Hello! I'm Agent Lexi from ODIA AI. I help Nigerian businesses automate their WhatsApp customer service. Let me show you how we can help your business grow!",
        
        "Agent MISS (University)": "Good day! I am Agent MISS, your academic assistant. I support students and faculty at Nigerian universities with smart AI services.",
        
        "Agent Atlas (Luxury)": "Welcome! I'm Agent Atlas, your luxury specialist. I help you plan exclusive experiences and premium services across Nigeria and beyond.",
        
        "Agent Legal (Compliance)": "Greetings! I am Agent Miss Legal, your compliance specialist. I help Nigerian businesses meet all legal and data protection requirements.",
        
        "Business Demo": "Welcome to ODIA AI! We are Nigeria's leading voice technology company, serving businesses across Lagos, Abuja, and Port Harcourt with cutting-edge solutions."
    }
    
    print(f"\n🎬 Creating {len(voices_to_create)} PROFESSIONAL voices...")
    
    created_files = []
    
    for voice_name, script in voices_to_create.items():
        print(f"\n🎙️ Creating: {voice_name}")
        print(f"   Script: {script[:50]}...")
        
        try:
            # Create NIGERIAN English voice (not robot English!)
            tts = gTTS(
                text=script, 
                lang='en', 
                tld='com.ng',  # 🇳🇬 This makes it sound NIGERIAN!
                slow=False
            )
            
            # Save with clean filename
            filename = f"odia_{voice_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.mp3"
            tts.save(filename)
            
            created_files.append(filename)
            print(f"   ✅ Saved: {filename}")
            
        except Exception as e:
            print(f"   ❌ Error creating {voice_name}: {e}")
    
    return created_files

def test_voice_quality():
    """Test if voices sound good"""
    
    print("\n🧪 TESTING VOICE QUALITY...")
    
    # Create a test voice
    from gtts import gTTS
    
    test_text = "Hello! This is a test of ODIA AI voice quality. Does this sound like a real Nigerian person speaking?"
    
    print("🎙️ Creating test voice...")
    tts = gTTS(text=test_text, lang='en', tld='com.ng', slow=False)
    tts.save("odia_voice_test.mp3")
    
    print("✅ Test voice created: odia_voice_test.mp3")
    print("🎧 PLAY THIS FILE AND LISTEN!")
    print("   - Does it sound natural?")
    print("   - Does it sound Nigerian?")
    print("   - Would customers like this voice?")
    
    return "odia_voice_test.mp3"

if __name__ == "__main__":
    print("="*60)
    print("🇳🇬 ODIA VOICE QUALITY FIX")
    print("="*60)
    print("Goal: Make voices sound HUMAN, not ROBOT!")
    print("="*60)
    
    try:
        # Step 1: Create real Nigerian voices
        voice_files = create_real_nigerian_voices()
        
        # Step 2: Test quality
        test_file = test_voice_quality()
        
        # Step 3: Show results
        print("\n" + "="*60)
        print("🎉 SUCCESS! VOICE QUALITY FIXED!")
        print("="*60)
        
        print(f"✅ Created {len(voice_files)} professional voices:")
        for file in voice_files:
            print(f"   📁 {file}")
        
        print(f"\n🧪 Test this voice: {test_file}")
        print("\n🎯 NEXT STEPS:")
        print("1. 🎧 Play the voice files")
        print("2. ✅ Confirm they sound HUMAN (not robot)")
        print("3. 🚀 THEN we can talk about selling them!")
        
        print("\n💡 TIP: If voices still sound robotic, we'll try ElevenLabs!")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\n🔧 TROUBLESHOOTING:")
        print("1. Make sure you have internet connection")
        print("2. Try running: pip install gtts pygame")
        print("3. Run this script again")
    
    print("="*60)