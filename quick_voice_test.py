import torch
import chatterbox
print("🚀 ODIA Nigerian Voice Test")
print(f"✅ GPU: {torch.cuda.get_device_name^(0^)}")
print("📥 Loading voice maker...")
tts = chatterbox.ChatterboxTTS.from_pretrained("resemble-ai/chatterbox")
print("✅ Voice maker ready!")
text = "Hello! Welcome to ODIA AI, Nigeria's premier voice technology company. We provide cutting-edge text-to-speech solutions for businesses across Africa."
print("🎙️ Creating Nigerian business voice...")
audio = tts.generate(text)
audio.save("odia_nigerian_voice.wav")
print("✅ SUCCESS! Voice saved as: odia_nigerian_voice.wav")
print("💰 This voice is worth ₦0.50 per 1000 characters!")
print("🇳🇬 Ready to sell to Nigerian businesses!")
print("🎵 Double-click the .wav file to play it!")
