import requests
import json

url = "https://superheroapi.com/api/4322227127822277/491"
response = requests.request("GET", url)
json_data = json.loads(response.text)

#sprawdzanie kluczy
expected = ['response', 'id', 'name', 'powerstats', 'biography', 'appearance', 'work', 'connections', 'image']
received = [k for k, v in json_data.items()]
assert expected == received
print(received)

#sprawdzenie wartości
for x in range(len(json_data)):
    assert type(x) == str or object
for x in json_data['powerstats']:
    x.isnumeric()

#sprawdzenie odpowiedzi
assert response.status_code == 200

#sprawdzenie niepoprawnego zapytania
url = "https://superheroapi.com/api/4322227127822277/999"
response = requests.request("GET", url)
json_data = json.loads(response.text)
print(response.status_code)
assert json_data['response'] == 'error'
print(json_data)

print('All tests passed')
