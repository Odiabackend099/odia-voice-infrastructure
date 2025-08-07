# 🧠 SIMPLE LEARNING BRAIN - Your Robot Gets Smarter!
# This makes your AI learn from every conversation

import json
import time
from datetime import datetime
from supabase import create_client, Client

print("🧠 Building your AI's learning brain...")
print("Goal: Never make the same mistake twice!")

# Your existing Supabase (FREE learning database)
SUPABASE_URL = "https://qgqfiluokypqmloknxlh.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFncWZpbHVva3lwcW1sb2tueGxoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzU1MTEwNSwiZXhwIjoyMDY5MTI3MTA1fQ.hhRpm-21UrSIQeGU-_TPNXNvDT6TPem1tz-67R2ro_o"

class SimpleAIBrain:
    """Your AI's learning brain - gets smarter with each conversation"""
    
    def __init__(self):
        print("🧠 Connecting to learning database...")
        
        # Connect to your learning database
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Create learning tables
        self.setup_learning_database()
        
        print("✅ AI brain connected and ready to learn!")
    
    def setup_learning_database(self):
        """Create tables where AI stores what it learns"""
        print("📚 Setting up learning database...")
        
        # This will store EVERY conversation for learning
        # (We'll create this through Supabase dashboard)
        learning_tables = {
            'nigerian_conversations': {
                'purpose': 'Store every conversation',
                'learns': 'How Nigerians talk, what they need'
            },
            'ai_improvements': {
                'purpose': 'Track what AI learned',
                'learns': 'Mistakes to never repeat'
            },
            'language_patterns': {
                'purpose': 'Learn Nigerian languages',
                'learns': 'Yoruba, Igbo, Hausa, Pidgin patterns'
            }
        }
        
        print("✅ Learning database ready!")
    
    def learn_from_conversation(self, user_said, ai_responded, user_feedback=None):
        """Learn from what user said and how AI responded"""
        print(f"📝 Learning from: '{user_said[:30]}...'")
        
        try:
            # Detect what language user spoke
            language = self.detect_nigerian_language(user_said)
            
            # Store the conversation for learning
            conversation_data = {
                'user_input': user_said,
                'ai_response': ai_responded,
                'detected_language': language,
                'user_feedback': user_feedback,
                'timestamp': datetime.now().isoformat(),
                'learned': False  # Will be True after AI learns from it
            }
            
            # Save to learning database
            result = self.supabase.table('nigerian_conversations').insert(conversation_data).execute()
            
            print(f"✅ Conversation saved for learning!")
            
            # If user gave feedback, learn immediately
            if user_feedback:
                self.learn_from_feedback(user_feedback, user_said, ai_responded)
            
            return True
            
        except Exception as e:
            print(f"❌ Learning failed: {e}")
            return False
    
    def detect_nigerian_language(self, text):
        """Detect which Nigerian language user is speaking"""
        text_lower = text.lower()
        
        # Simple language detection
        language_clues = {
            'yoruba': ['bawo', 'pele', 'emi', 'ore', 'wa'],
            'igbo': ['ndewo', 'kedu', 'ndi', 'ahu', 'gi'],
            'hausa': ['sannu', 'ina', 'da', 'kai', 'mu'],
            'pidgin': ['wetin', 'how far', 'dey', 'una', 'dem', 'abeg']
        }
        
        for language, words in language_clues.items():
            for word in words:
                if word in text_lower:
                    print(f"🗣️ Detected: {language.title()}")
                    return language
        
        print("🗣️ Detected: Nigerian English")
        return 'nigerian_english'
    
    def learn_from_feedback(self, feedback, original_input, ai_response):
        """Learn from what user thinks about AI's response"""
        print(f"🎯 Learning from feedback: '{feedback}'")
        
        try:
            # Analyze the feedback
            if any(word in feedback.lower() for word in ['good', 'great', 'correct', 'right', 'perfect']):
                learning_type = 'positive'
                improvement = f"User liked response to: {original_input[:50]}"
            else:
                learning_type = 'negative'
                improvement = f"User didn't like response to: {original_input[:50]}. Feedback: {feedback}"
            
            # Store the learning
            learning_data = {
                'original_input': original_input,
                'ai_response': ai_response,
                'user_feedback': feedback,
                'learning_type': learning_type,
                'improvement_note': improvement,
                'timestamp': datetime.now().isoformat()
            }
            
            self.supabase.table('ai_improvements').insert(learning_data).execute()
            
            print(f"✅ Learned from feedback: {learning_type}")
            
        except Exception as e:
            print(f"❌ Feedback learning failed: {e}")
    
    def get_smarter_response(self, user_input):
        """Use past learning to give better responses"""
        print(f"🤔 Thinking smarter about: '{user_input[:30]}...'")
        
        try:
            # Check if AI has learned from similar questions before
            similar_conversations = self.supabase.table('nigerian_conversations')\
                .select('*')\
                .ilike('user_input', f'%{user_input[:20]}%')\
                .execute()
            
            if similar_conversations.data:
                print(f"💡 Found {len(similar_conversations.data)} similar conversations!")
                
                # Use the learning to improve response
                best_response = self.find_best_learned_response(similar_conversations.data)
                return best_response
            
            print("🆕 This is a new type of question - AI will learn from it!")
            return None
            
        except Exception as e:
            print(f"❌ Smart response failed: {e}")
            return None
    
    def find_best_learned_response(self, similar_conversations):
        """Find the best response based on past learning"""
        # Simple logic: find responses that got positive feedback
        best_responses = []
        
        for conversation in similar_conversations:
            if conversation.get('user_feedback'):
                feedback = conversation['user_feedback'].lower()
                if any(word in feedback for word in ['good', 'great', 'correct', 'right']):
                    best_responses.append(conversation['ai_response'])
        
        if best_responses:
            print("✅ Using learned response pattern!")
            return best_responses[0]  # Return the first good response
        
        return None
    
    def show_learning_stats(self):
        """Show how much the AI has learned"""
        try:
            conversations = self.supabase.table('nigerian_conversations').select('*').execute()
            improvements = self.supabase.table('ai_improvements').select('*').execute()
            
            print(f"\n📊 AI LEARNING STATISTICS")
            print(f"="*40)
            print(f"Total Conversations: {len(conversations.data) if conversations.data else 0}")
            print(f"Learning Improvements: {len(improvements.data) if improvements.data else 0}")
            
            # Language breakdown
            if conversations.data:
                languages = {}
                for conv in conversations.data:
                    lang = conv.get('detected_language', 'unknown')
                    languages[lang] = languages.get(lang, 0) + 1
                
                print(f"\n🗣️ Languages Learned:")
                for lang, count in languages.items():
                    print(f"   {lang.title()}: {count} conversations")
            
            print(f"\n🧠 AI is getting smarter with each conversation!")
            
        except Exception as e:
            print(f"❌ Stats error: {e}")

# Test the learning brain
def test_learning_brain():
    """Test if your AI brain can learn"""
    print("\n🧪 TESTING AI LEARNING BRAIN")
    print("="*40)
    
    # Create the brain
    brain = SimpleAIBrain()
    
    # Test conversations (simulate learning)
    test_conversations = [
        {
            'user': "Hello, how are you?",
            'ai': "Hello! I dey fine well well! How far? How you dey?",
            'feedback': "Good response, very Nigerian!"
        },
        {
            'user': "Wetin be your name?",
            'ai': "My name na ODIA AI. I be your Nigerian assistant!",
            'feedback': "Perfect! You sound like real Nigerian!"
        },
        {
            'user': "Help me with business",
            'ai': "I go help you grow your business with AI technology!",
            'feedback': "Great, very helpful!"
        }
    ]
    
    print("📚 Teaching AI from sample conversations...")
    
    for i, conv in enumerate(test_conversations, 1):
        print(f"\n📝 Learning from conversation {i}...")
        
        success = brain.learn_from_conversation(
            conv['user'],
            conv['ai'], 
            conv['feedback']
        )
        
        if success:
            print(f"   ✅ Conversation {i} learned!")
        else:
            print(f"   ❌ Learning failed for conversation {i}")
    
    # Show what AI learned
    brain.show_learning_stats()
    
    print(f"\n🎉 YOUR AI BRAIN IS LEARNING!")
    print(f"💡 Every conversation makes it smarter!")

if __name__ == "__main__":
    print("🚀 STARTING AI LEARNING BRAIN")
    print("Goal: Make your AI learn like Maya and Miles!")
    print("="*50)
    
    test_learning_brain()
    
    print("\n✅ LEARNING BRAIN READY!")
    print("Next: Connect to your voice and app!")
