import requests

resp = requests.post("http://localhost:5000/predict?path=data/president.mp4")

print(resp.text)