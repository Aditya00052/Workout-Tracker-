import requests
from datetime import datetime

API_ID = "your_api_id"
API_KEY = "your_api_key"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Which exercise did you perform? "),
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 177,
    "age": 20
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()
print(data)

SHEETY_USERNAME = "enter_sheet_username"
SHEETY_PROJECT_NAME = "workoutTracking"
SHEETY_SHEET_NAME = "workouts"

sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

now = datetime.now()
date = f"{now.day}/{now.month}/{now.year}"  # or use now.strftime
time = now.time()
current_time = f"{time.hour}:{time.minute}:{time.second}"


for exercise in data["exercises"]:

    sheety_data = {
        "workout": {
            "date": date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": "Basic QWRpdHlhNTI6dWVibHVldmNodztvandpYw=="
    }

    response2 = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
    print(response2.text)

