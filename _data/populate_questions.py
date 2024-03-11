import json
import requests

if __name__ == '__main__':
    with open('questions/eng.json') as f:
        data = json.load(f)

    for question in data.get('questions', []):
        response = requests.post("http://localhost:8000/api/question",
                                 json={
                                     "text": question['text'],
                                     "level": question['level']
                                 })
        print(">>>>>>>>>", response.text)
