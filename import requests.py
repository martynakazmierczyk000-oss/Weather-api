import requests
#Dodawanie naszego klucza API

api_key='912b2e482a824a7688b81205250612'
city='Lublin' 

#Utworzenie zapytania do API OpenWeatherMap
url=f'https://api.weatherapi.com/v1/current.json?key=912b2e482a824a7688b81205250612&q=Warszawa&aqi=yes'

#Wykonuje zapytanie GET i pobierzemy dane w formacie JSON
response=requests.get(url)
response=response.json()

#Wyświetlamy pobrane dane
print(response)