import requests
APP_ID = "4b22b0e6"
API_KEY = "21415103ec65d4a55c1aff38a8340021"

GENDER = "female"
WEIGHT_KG = 63
HEIGHT_CM = 160
AGE = 30

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)