import requests
import unidecode
#Dodawanie naszego klucza API

api_key='912b2e482a824a7688b81205250612'

#Wybór miasta do sprawdzenia pogody
city=input('Podaj nazwę miasta, dla którego chcesz sprawdzić pogodę:')
city_unidecoded=unidecode.unidecode(city)

#Osobny komunikat 
input_message= (f'Wybierz co chcesz wyświetlić dla {city_unidecoded}: '
f'\n1. Temperatura'
f'\n2. Wilgotność'
f'\n3. Ciśnienie'
f'\n4. Warunki pogodowe'
f'\n5. Wszystkie informacje'
f'\nPodaj numer opcji: ')

#Zabezpieczenie przed wpisaniem wartości niebędącej liczbą
while True:
    try: 
        user_choice=int(input(input_message))
        if user_choice>=1 and user_choice<=5:
            break
        else:
            print('Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.')
    except ValueError:
        print('Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.')

#Zabezpieczenie przed wpisaniem wartości spoza zakresu
while user_choice<1 or user_choice>5:
    print('Nieprawidłowy wybór. Proszę wybrać numer od 1 do 5.')
    user_choice=int(input(input_message))

#Utworzenie zapytania do API OpenWeatherMap
url=f'https://api.weatherapi.com/v1/current.json?key=912b2e482a824a7688b81205250612&q={city_unidecoded}&aqi=yes'

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