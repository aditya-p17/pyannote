import requests
from dotenv import load_dotenv
import os

API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"


load_dotenv()

# Get the API key from the environment variables
API = os.getenv("API")
headers = {"Authorization": f"Bearer {API}"}



def query_sentiment(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

    




API_URL_SOUND = "https://api-inference.huggingface.co/models/Baghdad99/saad-speech-recognition-hausa-audio-to-text"
headers = {"Authorization": f"Bearer {API}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL_SOUND, headers=headers, data=data)
    return response.json()

output = query("2.mp3")
text = str(output["text"])
print(text)

senti = query_sentiment({
    "inputs": text
})

print(senti[0][0])



#File upload
#transcript
#transcript ka sentiment analysis


#transcript ka print basically pyannote jaisa ho --- dialogue by dialogue  -- taaki user output zyada readable ho