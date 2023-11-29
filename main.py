import requests
from datetime import datetime

APP_ID = 'your APP_ID'
API_KEY = 'your API_KEY'
TRACK_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEET_ENDPOINT = 'https://api.sheety.co/ee6dd7e9a3995a11d7e530e421efccb9/myWorkouts/workouts'
TOKEN = 'your TOKEN'

query = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    'query': query
}

response = requests.post(url=TRACK_ENDPOINT, json=params, headers=headers)

time = str(datetime.time(datetime.now()).strftime('%H:%M:%S'))
date = str(datetime.date(datetime.now()))

bearer_headers = {
    'Authorization': TOKEN
}

body = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': response.json()['exercises'][0]['name'],
        'duration': response.json()['exercises'][0]['duration_min'],
        'calories': response.json()['exercises'][0]['nf_calories']
    }
}

response = requests.post(url=SHEET_ENDPOINT, json=body, headers=bearer_headers)
print(response.text)
