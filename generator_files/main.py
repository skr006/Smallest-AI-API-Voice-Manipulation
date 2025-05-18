import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API token
TOKEN = os.getenv("SMALLEST_TOKEN")
if not TOKEN:
    raise ValueError("SMALLEST_TOKEN not found in environment variables")

# API endpoint and parameters
URL = "https://waves-api.smallest.ai/api/v1/lightning/get_speech"
SAMPLE_RATE = 16000
VOICE_ID = "ram"
OUTPUT_FILE = "generator_files/intro.wav"


payload = {
    "text": "Hi, I am S Karthik Ram from Coimbatore, India. I am a software engineer and I am working on a project to generate audio files using Smallest.ai text-to-speech technology.",
    "voice_id": "raman",
    "sample_rate": 16000,
    "speed": 1.0,
    "language": "en",
    "add_wav_header": True,
    "transliterate": False,
    "remove_extra_silence": False
}
# Headers for authentication
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

try:
    with requests.post(URL, json=payload, headers=headers, timeout=60, stream=True) as response:
        if response.status_code == 200:
            with open(OUTPUT_FILE, 'wb') as wav_file:
                for chunk in response.iter_content(chunk_size=8192):
                    wav_file.write(chunk)
            print(f"Audio file saved as {OUTPUT_FILE}")
        else:
            print(f"Request failed: {response.status_code}, {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {str(e)}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Partial response: {e.response.text}")