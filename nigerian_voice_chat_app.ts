// Nigerian Voice Chat App - Free for All Nigerians
// Copy this to your Lovable project

import React, { useState, useRef, useEffect } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Mic, Play, Send, MessageCircle, Globe, Heart } from 'lucide-react';

interface Message {
  id: number;
  text: string;
  isUser: boolean;
  audioUrl?: string;
  language: string;
  timestamp: Date;
  location?: string;
}

interface LearningStats {
  totalConversations: number;
  languagesLearned: string[];
  improvementScore: number;
}

const NigerianVoiceChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isRecording, setIsRecording] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [textInput, setTextInput] = useState('');
  const [userLocation, setUserLocation] = useState('Nigeria');
  const [learningStats, setLearningStats] = useState<LearningStats>({
    totalConversations: 0,
    languagesLearned: ['English'],
    improvementScore: 0
  });
  
  const audioRef = useRef<HTMLAudioElement>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);

  // Your N8N webhook URL (replace with your actual N8N endpoint)
  const N8N_WEBHOOK_URL = "https://your-n8n-instance.app.n8n.cloud/webhook/nigerian-ai-chat";

  // Welcome message in multiple Nigerian languages
  useEffect(() => {
    const welcomeMessage: Message = {
      id: 0,
      text: "🇳🇬 Sannu! Ndewo! Bawo! Welcome to Nigeria's Learning AI! I'm here to learn from every Nigerian conversation. Chat with me in English, Yoruba, Igbo, Hausa, or Pidgin - completely FREE! Every chat makes me smarter! 😊",
      isUser: false,
      language: 'multilingual',
      timestamp: new Date()
    };
    setMessages([welcomeMessage]);
  }, []);

  const sendToLearningAI = async (userMessage: string) => {
    setIsLoading(true);
    
    try {
      // Send to your N8N backend with learning context
      const response = await fetch(N8N_WEBHOOK_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_message: userMessage,
          user_location: userLocation,
          timestamp: new Date().toISOString(),
          learning_mode: true,
          free_for_nigerians: true
        })
      });
      
      const result = await response.json();
      
      // Add AI response to chat
      const aiMessage: Message = {
        id: Date.now() + 1,
        text: result.ai_response,
        isUser: false,
        audioUrl: result.voice_url,
        language: result.detected_language || 'english',
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, aiMessage]);
      
      // Update learning stats
      if (result.learning_stats) {
        setLearningStats(result.learning_stats);
      }
      
    } catch (error) {
      console.error('Error talking to Nigerian AI:', error);
      
      // Friendly Nigerian error message
      const errorMessage: Message = {
        id: Date.now() + 1,
        text: "Chai! Sorry my friend, I get small problem. Make you try again abeg! 🙏",
        isUser: false,
        language: 'pidgin',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    }
    
    setIsLoading(false);
  };

  const handleSendText = () => {
    if (!textInput.trim()) return;
    
    // Add user message to chat
    const userMessage: Message = {
      id: Date.now(),
      text: textInput,
      isUser: true,
      language: 'auto-detect',
      timestamp: new Date(),
      location: userLocation
    };
    
    setMessages(prev => [...prev, userMessage]);
    
    // Send to learning AI
    sendToLearningAI(textInput);
    
    // Clear input
    setTextInput('');
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorderRef.current = mediaRecorder;
      
      let audioChunks: BlobPart[] = [];
      
      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };
      
      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        
        // Convert speech to text (you'll add this)
        // For now, let's simulate
        const simulatedText = "Voice message received - speech-to-text coming soon!";
        setTextInput(simulatedText);
      };
      
      mediaRecorder.start();
      setIsRecording(true);
      
    } catch (error) {
      console.error('Error accessing microphone:', error);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const playAudio = (audioUrl: string) => {
    if (audioRef.current) {
      audioRef.current.src = audioUrl;
      audioRef.current.play();
    }
  };

  const giveFeedback = (messageId: number, rating: number) => {
    // Send feedback to learning system
    fetch(N8N_WEBHOOK_URL + '/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        conversation_id: messageId,
        rating: rating,
        feedback: rating >= 4 ? 'Good response' : 'Needs improvement'
      })
    });
  };

  const getLanguageFlag = (language: string) => {
    const flags = {
      'english': '🇬🇧',
      'yoruba': '🟢',
      'igbo': '🔴',
      'hausa': '⚪',
      'pidgin': '🇳🇬',
      'multilingual': '🌍'
    };
    return flags[language as keyof typeof flags] || '🇳🇬';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-white to-green-50 p-4">
      {/* Header */}
      <div className="max-w-2xl mx-auto mb-6">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-green-800 mb-2">
            🇳🇬 Nigeria's Learning AI
          </h1>
          <p className="text-gray-600 mb-2">
            Free voice AI for all Nigerians • Learning from every conversation
          </p>
          <div className="flex justify-center items-center gap-4 text-sm text-gray-500">
            <span className="flex items-center gap-1">
              <Globe className="w-4 h-4" />
              {learningStats.languagesLearned.length} Languages
            </span>
            <span className="flex items-center gap-1">
              <MessageCircle className="w-4 h-4" />
              {learningStats.totalConversations} Conversations
            </span>
            <span className="flex items-center gap-1">
              <Heart className="w-4 h-4 text-red-500" />
              FREE Forever
            </span>
          </div>
        </div>
      </div>

      {/* Language Support Banner */}
      <div className="max-w-2xl mx-auto mb-4">
        <div className="bg-green-100 border border-green-300 rounded-lg p-3 text-center">
          <p className="text-green-800 text-sm">
            🗣️ <strong>Speak any Nigerian language:</strong> English • Yoruba • Igbo • Hausa • Pidgin
          </p>
        </div>
      </div>

      {/* Chat Messages */}
      <div className="max-w-2xl mx-auto">
        <Card className="h-96 overflow-y-auto mb-4 border-2 border-green-200">
          <CardContent className="p-4 space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-xs lg:max-w-md px-4 py-3 rounded-lg shadow-sm ${
                    message.isUser
                      ? 'bg-green-600 text-white'
                      : 'bg-white border border-gray-200 text-gray-800'
                  }`}
                >
                  {/* Language indicator */}
                  {!message.isUser && (
                    <div className="flex items-center gap-2 mb-2 text-xs text-gray-500">
                      <span>{getLanguageFlag(message.language)}</span>
                      <span>{message.language}</span>
                    </div>
                  )}
                  
                  <p className="leading-relaxed">{message.text}</p>
                  
                  {/* Audio play button for AI responses */}
                  {!message.isUser && message.audioUrl && (
                    <div className="flex items-center gap-2 mt-3">
                      <Button
                        variant="ghost"
                        size="sm"
                        className="h-8 px-2 text-blue-600 hover:text-blue-800"
                        onClick={() => playAudio(message.audioUrl!)}
                      >
                        <Play className="w-4 h-4 mr-1" />
                        Play Voice
                      </Button>
                    </div>
                  )}
                  
                  {/* Feedback buttons for AI responses */}
                  {!message.isUser && message.id > 0 && (
                    <div className="flex gap-1 mt-2">
                      <button 
                        onClick={() => giveFeedback(message.id, 5)}
                        className="text-xs text-green-600 hover:text-green-800"
                      >
                        👍 Good
                      </button>
                      <button 
                        onClick={() => giveFeedback(message.id, 2)}
                        className="text-xs text-red-600 hover:text-red-800"
                      >
                        👎 Improve
                      </button>
                    </div>
                  )}
                  
                  <p className="text-xs opacity-70 mt-2">
                    {message.timestamp.toLocaleTimeString()}
                  </p>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-white border border-gray-200 px-4 py-3 rounded-lg">
                  <div className="flex items-center space-x-2">
                    <div className="animate-pulse">🧠</div>
                    <span>Nigerian AI is thinking...</span>
                  </div>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Location Selection */}
        <div className="mb-4">
          <select 
            value={userLocation} 
            onChange={(e) => setUserLocation(e.target.value)}
            className="w-full px-3