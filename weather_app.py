import requests
#Dodawanie naszego klucza API

api_key='912b2e482a824a7688b81205250612'

#Wybór miasta do sprawdzenia pogody
city=input('Podaj nazwę miasta, dla którego chcesz sprawdzić pogodę:')

user_choice=int(input(f'Wybierz co chcesz wyświetlić dla {city}: '
                      f'\n1. Temperatura'
                      f'\n2. Wilgotność'
                      f'\n3. Ciśnienie'
                      f'\n4. Warunki pogodowe'
                      f'\n5. Wszystkie informacje'
                      f'\nPodaj numer opcji: '))

#Utworzenie zapytania do API OpenWeatherMap
url=f'https://api.weatherapi.com/v1/current.json?key=912b2e482a824a7688b81205250612&q={city}&aqi=yes'

#Wykonuje zapytanie GET i pobierzemy dane w formacie JSON
response=requests.get(url)
response=response.json()

#Wyświetlamy pobrane dane
#print(response)

#Wyświetlenie wybranej opcji
if user_choice==1:
    print(f'Temperatura dla miasta {city} wynosi {response["current"]["temp_c"]}°C')
elif user_choice==2:
    print(f'Wilgotność powietrza dla masta {city} wynosi {response["current"]["humidity"]}%')   
elif user_choice==3:
    print(f'Ciśnienie dla miasta {city} wynosi {response["current"]["pressure_mb"]} hPa')
elif user_choice==4:
    weather_condition=response['current']['condition']['text']
    print(f'Warunki pogodowe dla miasta {city} to {weather_condition}')
elif user_choice==5:
    print(f'Temperatura dla miasta {city} wynosi {response["current"]["temp_c"]}°C')
    print(f'Wilgotność powietrza dla masta {city} wynosi {response["current"]["humidity"]}%')
    print(f'Ciśnienie dla miasta {city} wynosi {response["current"]["pressure_mb"]} hPa')
    weather_condition=response['current']['condition']['text']
    print(f'Warunki pogodowe dla miasta {city} to {weather_condition}')
else:
    print('Nieprawidłowy wybór opcji.')

#Wyświetlenie szczegółowych elementów
#print(f'Temperatura dla miasta {city} wynosi {response["current"]["temp_c"]}°C')
#print(f'Wilgotność powietrza dla masta {city} wynosi {response["current"]["humidity"]}%')
#print(f'Ciśnienie dla miasta {city} wynosi {response["current"]["pressure_mb"]} hPa')

#Informacje ogolne o pogodzie
#weather_condition=response['current']['condition']['text']
#print(f'Warunki pogodowe dla miasta {city} to {weather_condition}')