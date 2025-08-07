# 🚀 MAYA-LEVEL TTS INSTALLATION GUIDE
# Follow these steps to get HUMAN-LIKE voices!

echo "🔥 Installing Maya-Level TTS System..."
echo "Goal: Make voices sound like REAL HUMANS, not robots!"

# Step 1: Install Python packages
echo "📥 Step 1: Installing voice engines..."

# Basic requirements
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121  # RTX 4090 support
pip install transformers
pip install numpy
pip install asyncio

# Advanced TTS engines (choose the best available)
echo "🎙️ Installing advanced TTS engines..."

# Option 1: Coqui TTS (BEST for emotions)
pip install TTS

# Option 2: Fallback options
pip install pyttsx3  # Basic TTS
pip install gtts     # Google TTS (good Nigerian accent)

# Option 3: Advanced models (if you want Sesame CSM-1B)
pip install transformers[torch]
pip install torchaudio

echo "✅ Installation complete!"

# Step 2: Test your GPU
echo "🔥 Testing RTX 4090..."
python -c "
import torch
if torch.cuda.is_available():
    print(f'✅ GPU: {torch.cuda.get_device_name(0)}')
    print(f'🧠 VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB')
    if '4090' in torch.cuda.get_device_name(0):
        print('💪 PERFECT! RTX 4090 ready for Maya-level voices!')
    else:
        print('⚠️ Not RTX 4090 but will work')
else:
    print('❌ No GPU detected!')
"

echo "🎯 Next: Run the Maya TTS system!"
echo "Command: python maya_tts_system.py"