import os
import requests

def generate_speech(text):

    print("text",text)

    XI_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
    VOICE_ID = os.environ.get('VOICE_ID')
    TEXT_TO_SPEAK = text
    
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": TEXT_TO_SPEAK,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    response = requests.post(tts_url, headers=headers, json=data, stream=True)

    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()
