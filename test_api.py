import requests 
BASE_URL = 'https://api.open-meteo.com/v1/forecast?'
params = ['latitude=', 'longitude=', 'start_date=', 'end_date=', 'models=', 'hourly=', 'timezone=']
URL = BASE_URL
for x in params:
    param = x + str(input(f'{x}: ')) + '&'
    URL += param
print(URL)
response = requests.get(URL)
print(response)  