import requests

# URL de l'API Open-Meteo
url = "https://climate-api.open-meteo.com/v1/climate"

# Paramètres : 1 seule année, 1 modèle, pour ne pas épuiser le quota partagé de l'IUT
parametres = {
    "latitude": 43.60,
    "longitude": 1.44,
    "start_date": "2049-01-01",
    "end_date": "2049-12-31",
    "models": "MRI_AGCM3_2_S",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Europe/Paris"
}

print("Envoi de la requête à l'API...")
reponse = requests.get(url, params=parametres)

if reponse.status_code == 200:
    donnees = reponse.json()
    print("Succès ! L'API répond bien.")
    print("Dates récupérées :", donnees["daily"]["time"][:5])
    print("T_max récupérées :", donnees["daily"]["temperature_2m_max"][:5])
else:
    print(f"Erreur {reponse.status_code}: {reponse.text}")