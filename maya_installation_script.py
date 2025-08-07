# 🔥 MAYA-LEVEL VOICE INSTALLATION FOR WINDOWS
# Save this as: maya_installer.py

import subprocess
import sys
import os
import time

def install_maya_voices():
    """
    Install Maya-level voices on Windows - SUPER EASY!
    """
    print("🚀 MAYA-LEVEL VOICE INSTALLER FOR WINDOWS")
    print("="*60)
    print("Goal: Make your AI sound like a REAL HUMAN!")
    print("Time: 5-10 minutes")
    print("="*60)
    
    # Check if we're on Windows
    if os.name != 'nt':
        print("❌ This is for Windows only!")
        return False
    
    print("✅ Windows detected!")
    
    # Check Python
    try:
        python_version = sys.version
        print(f"✅ Python found: {python_version.split()[0]}")
    except:
        print("❌ Python not found!")
        return False
    
    # Step 1: Install basic requirements
    print("\n📦 STEP 1: Installing voice foundations...")
    print("This might take 2-3 minutes...")
    
    basic_packages = [
        "torch",           # Neural networks
        "torchaudio",      # Audio processing
        "numpy",           # Math
        "requests",        # Web requests
        "fastapi",         # API server
        "uvicorn",         # Server runner
    ]
    
    print("Installing basic packages...")
    for package in basic_packages:
        try:
            print(f"   Installing {package}...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", package, "--quiet"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"   ✅ {package} - SUCCESS!")
            else:
                print(f"   ⚠️ {package} - Had issues but continuing...")
                
        except Exception as e:
            print(f"   ⚠️ {package} - Error: {e}")
    
    # Step 2: Try advanced TTS
    print("\n🎙️ STEP 2: Installing voice engines...")
    print("This is where the magic happens!")
    
    # Try Google TTS (most reliable)
    print("\n   🌍 Installing Google TTS (Nigerian accent)...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "gtts", "pygame", "--quiet"
        ], check=True, timeout=180)
        print("   ✅ Google TTS - SUCCESS! (Nigerian voices ready)")
        has_gtts = True
    except:
        print("   ⚠️ Google TTS - Issues")
        has_gtts = False
    
    # Try advanced TTS
    print("\n   🔥 Installing Advanced TTS...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "TTS", "--quiet"
        ], check=True, timeout=300)
        print("   ✅ Advanced TTS - SUCCESS! (Maya-level voices)")
        has_advanced = True
    except:
        print("   ⚠️ Advanced TTS - Issues (Google TTS will work)")
        has_advanced = False
    
    # Try Windows TTS
    print("\n   🪟 Installing Windows TTS...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "pyttsx3", "--quiet"
        ], check=True, timeout=120)
        print("   ✅ Windows TTS - SUCCESS!")
        has_windows_tts = True
    except:
        print("   ⚠️ Windows TTS - Issues")
        has_windows_tts = False
    
    # Step 3: Test GPU
    print("\n🔥 STEP 3: Testing your RTX 4090...")
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            
            print(f"✅ GPU Found: {gpu_name}")
            print(f"✅ GPU Memory: {gpu_memory:.1f}GB")
            
            if "4090" in gpu_name:
                print("🔥 RTX 4090 DETECTED! PERFECT FOR MAYA VOICES!")
                gpu_ready = True
            else:
                print("✅ GPU ready for voice AI!")
                gpu_ready = True
        else:
            print("⚠️ No GPU detected - will use CPU (slower)")
            gpu_ready = False
    except:
        print("⚠️ GPU test failed - continuing with CPU")
        gpu_ready = False
    
    # Results
    total_engines = sum([has_gtts, has_advanced, has_windows_tts])
    
    print(f"\n🎉 INSTALLATION COMPLETE!")
    print("="*60)
    print(f"✅ Voice engines installed: {total_engines}/3")
    print(f"✅ GPU ready: {'YES' if gpu_ready else 'CPU mode'}")
    
    if has_gtts:
        print("✅ Google TTS - Nigerian accent voices")
    if has_advanced:
        print("✅ Advanced TTS - Maya-level quality") 
    if has_windows_tts:
        print("✅ Windows TTS - Local voices")
    
    if total_engines > 0:
        print(f"\n🚀 SUCCESS! Ready for human-like voices!")
        print(f"💰 Your AI can now sound like a real person!")
        
        # Create test script
        create_voice_test()
        
        print(f"\n🎯 NEXT STEP:")
        print(f"   Run: python voice_test.py")
        print(f"   This will show you the difference!")
        
        return True
    else:
        print(f"\n❌ Installation had issues.")
        print(f"💡 Try running this script again!")
        return False

def create_voice_test():
    """
    Create a simple test script
    """
    test_script = '''# 🧪 VOICE TEST - See the difference!

import time

def test_maya_voices():
    """Test your new Maya-level voices"""
    
    print("🧪 TESTING YOUR NEW MAYA-LEVEL VOICES")
    print("="*50)
    
    # Test Google TTS (Nigerian accent)
    print("\\n🌍 Testing Google TTS (Nigerian accent)...")
    try:
        from gtts import gTTS
        
        text = "Hello! Welcome to ODIA AI Nigeria! I'm Agent Lexi, and I'm absolutely thrilled to help your business grow with our cutting-edge AI solutions!"
        
        print(f"🎙️ Creating Nigerian voice...")
        tts = gTTS(text=text, lang='en', tld='com.ng', slow=False)
        tts.save("nigerian_voice_test.mp3")
        
        print("✅ SUCCESS! Created: nigerian_voice_test.mp3")
        print("🎧 Play this file - it sounds Nigerian!")
        
    except Exception as e:
        print(f"⚠️ Google TTS test failed: {e}")
    
    # Test Advanced TTS
    print("\\n🔥 Testing Advanced TTS...")
    try:
        from TTS.api import TTS
        
        print("📥 Loading advanced model...")
        tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
        
        text = "This is advanced artificial intelligence speaking with human-like quality!"
        
        print("🎙️ Creating advanced voice...")
        tts.tts_to_file(text=text, file_path="advanced_voice_test.wav")
        
        print("✅ SUCCESS! Created: advanced_voice_test.wav") 
        print("🎧 This sounds more human!")
        
    except Exception as e:
        print(f"⚠️ Advanced TTS test failed: {e}")
    
    # Test Windows TTS
    print("\\n🪟 Testing Windows TTS...")
    try:
        import pyttsx3
        
        engine = pyttsx3.init()
        
        # Try to find a good voice
        voices = engine.getProperty('voices')
        if voices:
            for voice in voices:
                if 'female' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
        
        engine.setProperty('rate', 180)  # Speaking speed
        
        text = "Hello from Windows Text to Speech! I am your local AI assistant."
        
        print("🎙️ Creating Windows voice...")
        engine.save_to_file(text, "windows_voice_test.wav")
        engine.runAndWait()
        
        print("✅ SUCCESS! Created: windows_voice_test.wav")
        print("🎧 Your local Windows voice!")
        
    except Exception as e:
        print(f"⚠️ Windows TTS test failed: {e}")
    
    print("\\n🎉 VOICE TEST COMPLETE!")
    print("="*50)
    print("🎧 Play the audio files to hear the difference!")
    print("💰 Ready to make money with human voices!")

if __name__ == "__main__":
    test_maya_voices()
'''
    
    with open("voice_test.py", "w") as f:
        f.write(test_script)
    
    print("✅ Created voice_test.py")

if __name__ == "__main__":
    print("Starting Maya voice installation...")
    time.sleep(2)  # Give user time to read
    
    success = install_maya_voices()
    
    if success:
        print("\\n🎯 READY TO TEST!")
        print("Run this command next:")
        print("   python voice_test.py")
    else:
        print("\\n💡 Try running this script again!")
        print("Sometimes Windows needs a second try!")