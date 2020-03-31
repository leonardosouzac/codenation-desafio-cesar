import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=bb51878d4210953f4059c0b7a72693bfb7dfaced"

answer = {'answer': open(r'C:\Users\Leonardo\Desktop\codenation_cesar\answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())