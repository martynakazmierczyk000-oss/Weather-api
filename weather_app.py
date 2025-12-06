import requests
#Dodawanie naszego klucza API

api_key='912b2e482a824a7688b81205250612'

#Wybór miasta do sprawdzenia pogody
city=input('Podaj nazwę miasta, dla którego chcesz sprawdzić pogodę:')

#Utworzenie zapytania do API OpenWeatherMap
url=f'https://api.weatherapi.com/v1/current.json?key=912b2e482a824a7688b81205250612&q={city}&aqi=yes'

#Wykonuje zapytanie GET i pobierzemy dane w formacie JSON
response=requests.get(url)
response=response.json()

#Wyświetlamy pobrane dane
#print(response)

#Wyświetlenie szczegółowych elementów
print(f'Temperatura dla miasta {city} wynosi {response["current"]["temp_c"]}°C')
print(f'Wilgotność powietrza dla masta {city} wynosi {response["current"]["humidity"]}%')
print(f'Ciśnienie dla miasta {city} wynosi {response["current"]["pressure_mb"]} hPa')

#Informacje ogolne o pogodzie
weather_condition=response['current']['condition']['text']
print(f'Warunki pogodowe dla miasta {city} to {weather_condition}')