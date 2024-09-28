import requests
from datetime import datetime

TOKEN = "xxxxx"
APP_ID = "xxxx"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": TOKEN
}
sheet_header = {
   "Content-Type": "application/json",
   "Authorization": "Bearer xxxxx"
}
exercise_input = {
    "query": input("what exercise you have done today?")
}
response = requests.post(url=API_ENDPOINT, json=exercise_input, headers=header)
data = response.json()
dt = datetime.now()
date = dt.strftime("%d/%m/%Y")
time = dt.strftime("%H:%M:%S")

for tag in range(len(data['exercises'])):
    print(data['exercises'][tag])
    duration = data['exercises'][tag]["duration_min"]
    exercise_name = data['exercises'][tag]["name"]
    calories = data['exercises'][tag]["nf_calories"]
    Sheet_URL = "https://api.sheety.co/xxxxxxx/nihaWorkouts/workouts"
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": int(duration),
            "calories": int(calories)
    }
    }
    response = requests.post(url=Sheet_URL, json=sheet_params, headers=sheet_header)
    print(response.text)

