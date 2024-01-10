import requests

API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"
headers = {"Authorization": f"Bearer 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"}

def query_sentiment(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
output=query_sentiment({
	"inputs": "Damn it's not working!!!"
})
	


print(output[0][0])

APT_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/Baghdad99/saad-speech-recognition-hausa-audio-to-text"
headers = {"Authorization": f"Bearer {APT_TOKEN}"}

def query_att(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
output1 = query_att("1.mp3")
text=str(output1["text"])
print(text)
# output = query_sentiment()
# print(output)


output=query_sentiment({
	"inputs": output1
})
print(output)
#File upload
#transcript
#transcript ka sentiment analysis


#transcript ka print basically pyannote jaisa ho --- dialogue by dialogue  -- taaki user output zyada readable ho