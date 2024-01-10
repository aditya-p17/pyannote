import requests
from dotenv import load_dotenv
import os

API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"
#headers = {"Authorization": f"Bearer {API} "}

# Load the .env file
load_dotenv()

# Get the API key from the environment variables
API = os.getenv("API")
headers = {"Authorization": f"Bearer {API}"}



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Frankly, my dear, I don't give a damn.",
})

print(output[0][0])

#File upload
#transcript
#transcript ka sentiment analysis


#transcript ka print basically pyannote jaisa ho --- dialogue by dialogue  -- taaki user output zyada readable ho