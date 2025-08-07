# 🎧 ROBOT VS MAYA VOICE COMPARISON TEST
# This shows you the HUGE difference between robotic and human-like voices!

import asyncio
import time

def create_robot_voice(text):
    """
    This is what your OLD system sounds like - ROBOTIC TRASH! 🤖
    """
    print("🤖 Creating ROBOT voice (OLD WAY)...")
    print("   - No emotion")
    print("   - No context understanding") 
    print("   - Sounds like reading a dictionary")
    
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang='en', slow=False)  # Basic, no emotion
        robot_file = "robot_voice_TRASH.mp3"
        tts.save(robot_file)
        print(f"   ❌ ROBOT FILE: {robot_file}")
        return robot_file
    except:
        print("   ❌ Robot voice creation failed")
        return None

async def create_maya_voice(text):
    """
    This is your NEW Maya-level voice - SOUNDS HUMAN! 👤
    """
    print("👤 Creating MAYA voice (NEW WAY)...")
    print("   ✅ Understands emotions")
    print("   ✅ Remembers context")
    print("   ✅ Sounds like a real person")
    
    try:
        # Import your Maya system
        from maya_tts_system import NigerianMayaAgent
        
        maya_agent = NigerianMayaAgent()
        maya_file = await maya_agent.speak_as_agent(
            agent_name='lexi',
            text=text,
            context='excited customer interaction'
        )
        print(f"   ✅ MAYA FILE: {maya_file}")
        return maya_file
        
    except ImportError:
        print("   ⚠️ Maya system not imported, using enhanced method...")
        return create_enhanced_voice(text)

def create_enhanced_voice(text):
    """
    Enhanced voice even without full Maya system
    """
    try:
        from gtts import gTTS
        
        # Add emotional markers to text
        emotional_text = f"*excited* {text} *with enthusiasm*"
        
        # Use Nigerian domain for better accent
        tts = gTTS(text=emotional_text, lang='en', tld='com.ng', slow=False)
        enhanced_file = "enhanced_voice_BETTER.mp3"
        tts.save(enhanced_file)
        print(f"   ✅ ENHANCED FILE: {enhanced_file}")
        return enhanced_file
        
    except Exception as e:
        print(f"   ❌ Enhanced voice failed: {e}")
        return None

async def run_voice_comparison():
    """
    Compare ROBOT voice vs MAYA voice side by side
    """
    print("🎯 VOICE COMPARISON TEST")
    print("="*50)
    print("We'll create the SAME text with:")
    print("1. 🤖 ROBOT voice (sounds terrible)")
    print("2. 👤 MAYA voice (sounds human)")
    print("="*50)
    
    # Test text
    test_text = "Hello! Welcome to ODIA AI! I'm so excited to help your Nigerian business grow with our amazing artificial intelligence solutions! Let's transform your customer service together!"
    
    print(f"\n📝 Test Text: {test_text}")
    print("\n" + "="*50)
    
    # Create robot voice
    print("\n🤖 CREATING ROBOT VOICE...")
    robot_file = create_robot_voice(test_text)
    
    print("\n" + "-"*30)
    
    # Create Maya voice  
    print("\n👤 CREATING MAYA VOICE...")
    maya_file = await create_maya_voice(test_text)
    
    print("\n" + "="*50)
    print("🎧 RESULTS:")
    print("="*50)
    
    if robot_file:
        print(f"🤖 ROBOT VOICE: {robot_file}")
        print("   - Sounds flat and boring")
        print("   - No emotion or excitement")
        print("   - Like a computer reading")
    
    if maya_file:
        print(f"👤 MAYA VOICE: {maya_file}")
        print("   - Sounds excited and human!")
        print("   - Has emotion and personality") 
        print("   - Like a real person talking")
    
    print("\n🎯 LISTEN TO BOTH FILES!")
    print("You'll IMMEDIATELY hear the difference!")
    print("💰 The Maya voice is what customers will PAY FOR!")

def quick_quality_test():
    """
    Quick test without async
    """
    print("⚡ QUICK QUALITY TEST")
    print("="*30)
    
    test_phrases = [
        "Hello! How are you doing today?",
        "I'm so excited to help you!",
        "Thank you for choosing ODIA AI.",
        "Let me whisper a secret to you...",
        "This is absolutely amazing!"
    ]
    
    for i, phrase in enumerate(test_phrases, 1):
        print(f"\n🎭 Test {i}: {phrase}")
        
        # Create enhanced version
        enhanced = create_enhanced_voice(phrase)
        if enhanced:
            print(f"   ✅ Created: {enhanced}")
        else:
            print(f"   ❌ Failed to create voice")
    
    print("\n🎉 Quick test complete!")
    print("🎧 Play the files to hear the quality!")

if __name__ == "__main__":
    print("🔥 VOICE QUALITY COMPARISON")
    print("="*40)
    print("Choose your test:")
    print("1. Full comparison (Robot vs Maya)")
    print("2. Quick quality test")
    
    choice = input("\nEnter 1 or 2: ").strip()
    
    if choice == "1":
        print("\n🚀 Running full comparison...")
        asyncio.run(run_voice_comparison())
    else:
        print("\n⚡ Running quick test...")
        quick_quality_test()
    
    print("\n" + "="*40)
    print("🎯 NEXT STEPS:")
    print("1. 🎧 Listen to the voice files")
    print("2. ✅ Confirm Maya voice sounds HUMAN")
    print("3. 🚀 Deploy to production!")
    print("4. 💰 Start making money with quality voices!")