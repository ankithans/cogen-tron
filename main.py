import requests

x = 3
y=requests.get(f"https://productrecommenderaaa.herokuapp.com/api/v1.0/recommendations/{x}")

for prod in y.json()['data']:
    print(f"{round(prod['frequency'] * 100, 1)}% of users also searched about {prod['name']}")