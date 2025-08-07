# test_voice.py - Copy this into notepad and save it

import torch
import chatterbox

print("🚀 Testing ODIA Nigerian Voice...")

# Check GPU
print(f"✅ GPU: {torch.cuda.get_device_name(0)}")

# Load voice maker
print("📥 Loading voice maker...")
tts = chatterbox.ChatterboxTTS(device="cuda")
print("✅ Voice maker ready!")

# Create a Nigerian business voice
text = "Hello! Welcome to ODIA AI, Nigeria's number one voice technology company."
print(f"🎙️ Creating voice: '{text}'")

audio = tts.generate(text)
audio.save("my_first_nigerian_voice.wav")

print("✅ DONE! Check for 'my_first_nigerian_voice.wav' file")
print("💰 You just created your first sellable voice!")