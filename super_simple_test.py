import torch 
print("?? ODIA Nigerian Voice Test Starting...") 
print(f"? GPU: {torch.cuda.get_device_name(0)}") 
 
try: 
    import chatterbox 
    print("? Chatterbox imported successfully") 
    print("?? Available functions:") 
    available = [item for item in dir(chatterbox) if not item.startswith('_')] 
    for item in available: 
        print(f"   - {item}") 
    print("??? Trying simple method...") 
    tts = chatterbox.ChatterboxTTS.from_pretrained("resemble-ai/chatterbox") 
    audio = tts.generate("Hello from ODIA AI Nigeria!") 
    audio.save("odia_voice.wav") 
    print("? SUCCESS! Voice saved!") 
except Exception as e: 
    print(f"? Error: {e}") 
    print("?? We can fix this!") 
