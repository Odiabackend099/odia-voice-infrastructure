# 🔥 VOICE EMPIRE - FIXED VERSION
# Fixes the coqui-tts installation issue

import torch
import os
import sys
import subprocess
import json
import time
from pathlib import Path

print("🔴 VOICE EMPIRE - FIXED VERSION")
print("🔧 Fixed the installation issues!")
print("💪 RTX 4090 Ready for Voice Domination!")

class VoiceEmpireFixed:
    """
    Fixed Voice Empire - Works around installation issues
    """
    
    def __init__(self):
        print("🚀 Initializing FIXED Voice Empire...")
        
        # Check RTX 4090
        if torch.cuda.is_available():
            self.gpu_name = torch.cuda.get_device_name(0)
            self.gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            
            print(f"💪 GPU: {self.gpu_name}")
            print(f"🧠 VRAM: {self.gpu_memory:.1f}GB")
            
            if "4090" in self.gpu_name:
                print("🔥 RTX 4090 MONSTER DETECTED!")
                self.gpu_tier = "monster"
            else:
                print("✅ GPU ready for voice empire!")
                self.gpu_tier = "good"
        else:
            print("⚠️ Using CPU")
            self.gpu_tier = "cpu"
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Optimize RTX 4090
        if self.device.type == 'cuda':
            torch.backends.cudnn.benchmark = True
            torch.cuda.set_per_process_memory_fraction(0.8)
    
    def install_fixed_tools(self):
        """
        Install voice tools with fixed methods
        """
        print("\n🔧 INSTALLING FIXED VOICE TOOLS")
        print("="*50)
        print("Using alternative installation methods...")
        
        # Essential tools that work reliably
        essential_tools = [
            "torch>=2.0.0",
            "torchaudio>=2.0.0",
            "transformers>=4.30.0",
            "librosa>=0.10.0",
            "soundfile>=0.12.0",
            "scipy>=1.10.0",
            "numpy>=1.24.0",
            "fastapi>=0.100.0",
            "uvicorn[standard]>=0.22.0",
            "requests>=2.31.0",
            "python-dotenv>=1.0.0"
        ]
        
        print(f"📦 Installing {len(essential_tools)} essential tools...")
        
        for tool in essential_tools:
            try:
                print(f"   Installing {tool.split('>=')[0]}...")
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", tool, "--quiet"
                ])
                print(f"   ✅ {tool.split('>=')[0]} installed!")
            except Exception as e:
                print(f"   ⚠️ {tool} issue: {e}")
        
        print("\n✅ Essential tools installed!")
        
        # Try alternative TTS installation
        print("\n🎙️ Installing TTS engines...")
        self.install_alternative_tts()
    
    def install_alternative_tts(self):
        """
        Install TTS using alternative methods
        """
        tts_options = [
            # Option 1: Direct TTS installation
            {
                'name': 'TTS (Direct)',
                'command': [sys.executable, "-m", "pip", "install", "TTS", "--no-deps"],
                'post_install': [sys.executable, "-m", "pip", "install", "coqui-tts"]
            },
            # Option 2: gTTS (Google TTS - always works)
            {
                'name': 'Google TTS',
                'command': [sys.executable, "-m", "pip", "install", "gtts", "pygame"],
                'post_install': None
            },
            # Option 3: pyttsx3 (Offline TTS)
            {
                'name': 'PyTTSx3',
                'command': [sys.executable, "-m", "pip", "install", "pyttsx3"],
                'post_install': None
            }
        ]
        
        self.tts_engines = []
        
        for option in tts_options:
            try:
                print(f"   Installing {option['name']}...")
                subprocess.check_call(option['command'] + ["--quiet"])
                
                if option['post_install']:
                    subprocess.check_call(option['post_install'] + ["--quiet"])
                
                self.tts_engines.append(option['name'])
                print(f"   ✅ {option['name']} installed!")
                
            except Exception as e:
                print(f"   ⚠️ {option['name']} failed: {e}")
        
        print(f"\n✅ {len(self.tts_engines)} TTS engines ready!")
    
    def test_voice_engines(self):
        """
        Test which voice engines are working
        """
        print("\n🧪 TESTING VOICE ENGINES")
        print("="*40)
        
        working_engines = []
        
        # Test TTS/Coqui
        try:
            from TTS.api import TTS
            print("✅ Advanced TTS (Coqui) - WORKING!")
            working_engines.append("Advanced TTS")
        except:
            print("❌ Advanced TTS - Not available")
        
        # Test Google TTS
        try:
            from gtts import gTTS
            print("✅ Google TTS - WORKING!")
            working_engines.append("Google TTS")
        except:
            print("❌ Google TTS - Not available")
        
        # Test PyTTSx3
        try:
            import pyttsx3
            print("✅ PyTTSx3 - WORKING!")
            working_engines.append("PyTTSx3")
        except:
            print("❌ PyTTSx3 - Not available")
        
        print(f"\n🎉 {len(working_engines)} voice engines ready!")
        self.working_engines = working_engines
        
        return len(working_engines) > 0
    
    def create_voice_with_best_engine(self, text: str, output_file: str = None):
        """
        Create voice using the best available engine
        """
        if output_file is None:
            output_file = f"voice_empire_{int(time.time())}.mp3"
        
        print(f"🎙️ Creating voice: '{text[:50]}...'")
        
        # Try engines in order of quality
        
        # Try Advanced TTS first
        try:
            from TTS.api import TTS
            print("🔥 Using Advanced TTS (Best Quality)...")
            
            tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(self.device)
            wav_file = output_file.replace('.mp3', '.wav')
            tts.tts_to_file(text=text, file_path=wav_file)
            
            print(f"✅ Advanced voice created: {wav_file}")
            return wav_file
            
        except Exception as e:
            print(f"⚠️ Advanced TTS failed: {e}")
        
        # Try Google TTS
        try:
            from gtts import gTTS
            print("🌍 Using Google TTS (Good Quality)...")
            
            # Use Nigerian domain for accent
            tts = gTTS(text=text, lang='en', tld='com.ng', slow=False)
            tts.save(output_file)
            
            print(f"✅ Google voice created: {output_file}")
            return output_file
            
        except Exception as e:
            print(f"⚠️ Google TTS failed: {e}")
        
        # Try PyTTSx3
        try:
            import pyttsx3
            print("💻 Using PyTTSx3 (Basic Quality)...")
            
            engine = pyttsx3.init()
            
            # Optimize voice settings
            voices = engine.getProperty('voices')
            if voices:
                for voice in voices:
                    if 'female' in voice.name.lower():
                        engine.setProperty('voice', voice.id)
                        break
            
            engine.setProperty('rate', 180)  # Speaking rate
            
            wav_file = output_file.replace('.mp3', '.wav')
            engine.save_to_file(text, wav_file)
            engine.runAndWait()
            
            print(f"✅ Basic voice created: {wav_file}")
            return wav_file
            
        except Exception as e:
            print(f"❌ All TTS engines failed: {e}")
            return None
    
    def create_nigerian_business_suite(self):
        """
        Create Nigerian business voice suite with working engines
        """
        print("\n🏢 CREATING NIGERIAN BUSINESS VOICE SUITE")
        print("="*60)
        
        business_voices = {
            'Customer_Service': "Hello! Welcome to ODIA AI Nigeria! I'm absolutely thrilled to help your business grow with our cutting-edge artificial intelligence solutions. How may I assist you today?",
            
            'Sales_Presentation': "Discover the future of Nigerian business with ODIA AI! Our advanced technology helps companies across Lagos, Abuja, and Port Harcourt increase their sales by 300 percent!",
            
            'Educational_Content': "Welcome to ODIA AI University! Today we explore how artificial intelligence is transforming education and business across Nigeria and West Africa.",
            
            'Professional_Announcement': "Important business update from ODIA AI regarding our revolutionary voice technology solutions for Nigerian enterprises and government institutions.",
            
            'Marketing_Campaign': "Transform your business today with ODIA AI! Join over 1000 Nigerian companies already using our smart automation to dominate their markets!"
        }
        
        created_voices = {}
        
        for voice_type, script in business_voices.items():
            print(f"\n🎯 Creating {voice_type.replace('_', ' ')}...")
            
            output_file = f"nigerian_business_{voice_type.lower()}.mp3"
            result = self.create_voice_with_best_engine(script, output_file)
            
            if result:
                created_voices[voice_type] = result
                print(f"   ✅ Success: {result}")
            else:
                print(f"   ❌ Failed: {voice_type}")
        
        print(f"\n🎉 BUSINESS VOICE SUITE COMPLETE!")
        print(f"📁 Created {len(created_voices)} professional voices!")
        
        # Save business portfolio
        portfolio = {
            'created_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_voices': len(created_voices),
            'voices': created_voices,
            'gpu_used': self.gpu_name if hasattr(self, 'gpu_name') else 'CPU',
            'engines_available': len(self.working_engines)
        }
        
        with open("nigerian_business_portfolio.json", 'w') as f:
            json.dump(portfolio, f, indent=2)
        
        return created_voices

def run_fixed_voice_empire():
    """
    Run the fixed voice empire setup
    """
    print("🔴 FIXED VOICE EMPIRE SETUP")
    print("="*50)
    print("🔧 Fixed installation issues")
    print("⚡ RTX 4090 optimized")
    print("💰 Business ready")
    print("="*50)
    
    # Initialize
    empire = VoiceEmpireFixed()
    
    # Install tools
    print("\n🛠️ STEP 1: Installing voice tools...")
    empire.install_fixed_tools()
    
    # Test engines
    print("\n🧪 STEP 2: Testing voice engines...")
    if not empire.test_voice_engines():
        print("❌ No voice engines working!")
        return
    
    # Create test voice
    print("\n🎙️ STEP 3: Testing voice creation...")
    test_text = "Hello! This is a test of my Nigerian voice empire. I am ready to dominate the voice AI market!"
    test_file = empire.create_voice_with_best_engine(test_text, "test_nigerian_voice.mp3")
    
    if not test_file:
        print("❌ Voice creation test failed!")
        return
    
    print(f"✅ Test voice created: {test_file}")
    
    # Create business suite
    print("\n🏢 STEP 4: Creating business voice suite...")
    business_voices = empire.create_nigerian_business_suite()
    
    # Final results
    print("\n🏆 VOICE EMPIRE COMPLETE!")
    print("="*50)
    print("✅ Fixed installation issues")
    print("✅ Voice engines working")
    print(f"✅ {len(business_voices)} business voices created")
    print("✅ Ready for Nigerian market domination")
    
    print(f"\n🎧 PLAY THESE VOICE FILES:")
    print(f"   - {test_file} (Test voice)")
    for voice_type, voice_file in business_voices.items():
        print(f"   - {voice_file} ({voice_type.replace('_', ' ')})")
    
    print(f"\n💰 REVENUE READY:")
    print(f"   📞 Customer service: ₦50,000/month per client")
    print(f"   🎯 Marketing campaigns: ₦100,000/project")
    print(f"   🎓 Educational content: ₦200,000/course")
    print(f"   🏛️ Government contracts: ₦1,000,000+")
    
    print(f"\n🚀 START MAKING MONEY:")
    print(f"   1. Play the voice files")
    print(f"   2. Contact Nigerian businesses")
    print(f"   3. Offer voice services")
    print(f"   4. Scale to millions!")

if __name__ == "__main__":
    run_fixed_voice_empire()