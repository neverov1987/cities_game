import random
"""
- Создать обход городов оканчивающихся на букву на которую больше нет городов по аналогиии с 'Ъ' и 'Ь' и убрать обход 'Ы'.
"""
debug = False  # set True to view list of cities
cities_repeat = []
select_regions = input("Выберите регион городов! \n 1.Россия \n 2.Весь мир \n Введите [1 или 2, По умолчанию Россия]:")
if select_regions == '1':
    city_file = 'cities_Russia'
    profile = 'Россия'
elif select_regions == '2':
    city_file = 'cities_all'
    profile = 'Весь мир'
else:
    city_file = 'cities_Russia'
    profile = 'Россия'
print(f"Текущий регион: {profile}")
with open(city_file) as f:
    city_file = f.readlines()
cities_upper = list(map(lambda x: x.strip(), city_file))
cities = [element.lower() for element in cities_upper]
last_character = ''

def check_city(input_city):
    global cities
    global cities_repeat
    global last_character
    input_lower = str(input_city.lower())
    if input_lower in cities:
        if input_lower[0] == last_character or not last_character:
            print(f"Город \"{input_lower.capitalize()}\" существует! ")
            cities_repeat.append(input_lower)
            cities.remove(input_lower)
            if input_lower[-1] == 'ь' or input_lower[-1] == 'ъ' or input_lower[-1] == 'ы':
                city_last_character = input_lower[-2]
                cities_with_first_character = [idx for idx in cities if idx[0].lower() == city_last_character.lower()]
                print(f"Городов на букву \"{city_last_character.upper()[0]}\":", len(cities_with_first_character))
                if debug:
                    print(cities_with_first_character)
                if not cities_with_first_character:
                    print(f"Городов на букву \"{city_last_character.upper()[0]}\" больше нет, ты победил!")
                    exit(0)
                else:
                    print(f"Мне город на: \"{city_last_character.upper()}\"")
            else:
                city_last_character = input_lower[-1]
                print(f"Мне город на: \"{city_last_character.upper()}\"")
                cities_with_first_character = [idx for idx in cities if idx[0].lower() == city_last_character.lower()]
                print(f"Городов на букву \"{city_last_character.upper()[0]}\":", len(cities_with_first_character))
                if not cities_with_first_character:
                    print("Ты победил!")
                    exit(0)
                if debug:
                    print(cities_with_first_character)  # Enable for debug
            new_city = [idx for idx in cities if idx[0].lower() == city_last_character.lower()]
            if not new_city:
                print("Ты победил!")
                exit(0)
            new_city = random.choice(new_city)
            cities_repeat.append(new_city)
            cities.remove(new_city)
            if new_city[-1] == 'ь' or new_city[-1] == 'ъ' or new_city[-1] == 'ы':
                last_character = new_city[-2]
            else:
                last_character = new_city[-1]
            print(f"Мой ответ: \"{new_city.capitalize()}\", тебе на: \"{last_character.upper()}\"")
            cities_with_first_character = [idx for idx in cities if idx[0].lower() == last_character.lower()]
            print(f"Городов на букву \"{last_character.upper()}\": {len(cities_with_first_character)} ")
            if not cities_with_first_character:
                print(f"Городов на букву \"{last_character.upper()}\" больше нет.")
                print("Ты проиграл!")
                exit(0)
            if debug:
                print(cities_with_first_character)  # Enable for debug
        elif input_lower[0] != last_character:
            print(f"Город \"{input_lower.capitalize()}\" не начинается на \"{last_character.upper()}\" Попробуй еще раз!")
    else:
        print(f"Города \"{input_lower.capitalize()}\" не существует. Попробуй еще раз!")

while True:
    city_input = input('Введите город: \n')
    city_input = city_input.lower()
    if city_input in cities:
        check_city(city_input)
    elif city_input in cities_repeat:
        print(f"Город \"{city_input.capitalize()}\" уже был! Попробуй еще раз")
    else:
        if not last_character:
            print(f"Город \"{city_input.capitalize()}\" не существует! Попробуй еще раз!")
        else:
            print(f"Город \"{city_input.capitalize()}\" не существует! Попробуй еще раз! Тебе на \"{last_character.upper()}\"")