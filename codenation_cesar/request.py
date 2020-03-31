import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=seu-token"

answer = {'answer': open(answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())
