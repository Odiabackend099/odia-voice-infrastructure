import torch 
import chatterbox 
 
print("?? ODIA Nigerian Voice Test - WORKING VERSION!") 
print(f"? GPU: {torch.cuda.get_device_name(0)}") 
 
print("?? Loading Chatterbox TTS...") 
try: 
    # Method 1: Try from_pretrained without device parameter 
    tts = chatterbox.ChatterboxTTS.from_pretrained("resemble-ai/chatterbox") 
    print("? Voice maker loaded successfully!") 
 
    # Create Nigerian business voice 
    text = "Welcome to ODIA AI, Nigeria's premier voice technology company." 
    print("??? Creating your first Nigerian voice...") 
 
    audio = tts.generate(text) 
    audio.save("odia_nigerian_business_voice.wav") 
 
    print("? SUCCESS! Your voice is ready!") 
    print("?? File saved as: odia_nigerian_business_voice.wav") 
    print("?? This voice is worth money!") 
    print("???? Ready to sell to Nigerian businesses!") 
 
except Exception as e: 
    print(f"? Error: {e}") 
    print("?? Let's try a different approach...") 
