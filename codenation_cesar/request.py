import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=seu-token"

answer = {'answer': open(r'C:\Users\Leonardo\Desktop\codenation_cesar\answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())
