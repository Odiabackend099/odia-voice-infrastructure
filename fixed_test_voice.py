import torch 
import chatterbox 
import time 
 
print("?? Testing ODIA Nigerian Voice...") 
print(f"? GPU: {torch.cuda.get_device_name(0)}") 
 
print("?? Loading voice maker...") 
try: 
    tts = chatterbox.ChatterboxTTS.from_pretrained("resemble-ai/chatterbox", device="cuda") 
    print("? Voice maker ready!") 
    text = "Hello! Welcome to ODIA AI, Nigeria's premier voice technology company." 
    print("??? Creating Nigerian business voice...") 
    audio = tts.generate(text) 
    audio.save("odia_nigerian_voice.wav") 
    print("? SUCCESS! Check for odia_nigerian_voice.wav") 
    print("?? You just made a sellable Nigerian voice!") 
except Exception as e: 
    print(f"? Error: {e}") 
    print("?? Trying backup method...") 
    tts = chatterbox.ChatterboxTTS() 
    audio = tts.generate("Hello from ODIA AI!") 
    audio.save("odia_test.wav") 
    print("? Backup voice created!") 
