import torch 
import chatterbox 
 
print("?? ODIA Nigerian Voice Test - FIXED VERSION!") 
print(f"? GPU: {torch.cuda.get_device_name(0)}") 
print("?? Loading Chatterbox TTS...") 
 
try: 
    tts = chatterbox.ChatterboxTTS.from_pretrained("resemble-ai/chatterbox") 
    print("? Voice maker loaded successfully!") 
    text = "Hello, welcome to ODIA AI Nigeria!" 
    print(f"??? Creating voice for: '{text}'") 
    audio = tts.generate(text) 
    audio.save("first_odia_voice.wav") 
    print("? SUCCESS! Your Nigerian voice is ready!") 
    print("?? File saved: first_odia_voice.wav") 
    print("?? Play it now - your AI can speak!") 
except Exception as e: 
    print(f"? Error details: {e}") 
    print("?? Let's try alternative method...") 
