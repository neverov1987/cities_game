'''
+Открыть фалй citys и загрузить в переменную (список)
+Сделать список в нижнем регистре
+сделать список с повтерениями (пустой)
Запрос города (str). Перевод в нижний регистр
сделать цикл
  - проверка в списке повторений
  - проерка в списке городов. При совпадении взять индекс и удалить город из списка
  - добавить в список повторений
  - Взть последнюю букву из введенного города в перемменную и слелать проход на поиск городов ничинающихся на эту букву в citys.
  - Сообщить "Отлично, такой город сущестовует /n Мне город на {последня буква в верхнем регистре}"
  - Произвести поиск по списку citys и найти слова начинающиеся на нужную букву.
  - Занести слово в список повторений и удалить из списка citys
  - Вывести сообщение "Я называю город {город}. Тебе на {последня буква в верхнем регистре}"
поменять litter на letter )))
'''
exit == 0
citys_repeat = []
import random
with open('citys_list') as f:
    city_file = f.readlines()
citys_upper = list(map(lambda x:x.strip(), city_file))
citys = [element.lower() for element in citys_upper] ; citys_upper
last_liter = ''
def check_city(input):
    global citys
    global citys_repeat
    global last_liter
    input = str(input)
    input_lower = input.lower()
    if input_lower in citys:
        if input_lower[0] == last_liter or last_liter == None or last_liter == '':
           print(f"Город {input_lower} есть в России")
           citys_repeat.append(input_lower)
           citys.remove(input_lower)
           if input_lower[-1] == 'ь' or input_lower[-1] == 'ъ' or input_lower[-1] == 'ы':
               city_last_litter = input_lower[-2]
               citys_with_first_litter = [idx for idx in citys if idx[0].lower() == city_last_litter.lower()]
               print(f"Городов на букву \"{city_last_litter.upper()[0]}\":", len(citys_with_first_litter))
               print(citys_with_first_litter)
               if citys_with_first_litter == 0:
                   print(f"Городов на букву \"{city_last_litter.upper()[0]}\" больше нет, ты победил!")
                   exit == 1
               else:
                   print(f"Мне город на: \"{city_last_litter.upper()}\"")
           else:
               city_last_litter = input_lower[-1]
               print(f"Мне город на: \"{city_last_litter.upper()}\"")
               citys_with_first_litter = [idx for idx in citys if idx[0].lower() == city_last_litter.lower()]
               print(f"Городов на букву \"{city_last_litter.upper()[0]}\":", len(citys_with_first_litter))
               if len(citys_with_first_litter) == 0:
                   print("Ты победил!")
                   exit(0)
               print(citys_with_first_litter)
           new_city = [idx for idx in citys if idx[0].lower() == city_last_litter.lower()]
           if new_city == []:
               print("Ты победил!")
               exit(0)
           new_city = random.choice(new_city)
           citys_repeat.append(new_city)
           citys.remove(new_city)
           if new_city[-1] == 'ь' or new_city[-1] == 'ъ' or new_city[-1] == 'ы':
               last_liter = new_city[-2]
           else:
               last_liter = new_city[-1]
           print(f"Мой ответ: {new_city}, тебе на: \"{last_liter.upper()}\"")
           citys_with_first_litter = [idx for idx in citys if idx[0].lower() == last_liter.lower()]
           print(f"Городов на букву \"{last_liter.upper()}\": {len(citys_with_first_litter)} ")
           if len(citys_with_first_litter) == 0:
               exit == 1
           print(citys_with_first_litter)
        elif input_lower[0] != last_liter:
           print(f"Город {input_lower} не начинается на \"{last_liter.upper()}\" Попробуй еще раз!")
    else:
        print(f"Города {input_lower} нет в России. Попробуй еще раз!")

while exit != 1:
    city_input = input('Введите город: \n')
    city_input = city_input.lower()
    # print(f"PRINT IN WHILE {city_input}")
    if city_input in citys:
        check_city(city_input)
    elif city_input in citys_repeat:
        print(f"Город {city_input} уже был! Попробуй еще раз")
    else:
        if last_liter == '' or last_liter == None:
            print(f"Город {city_input} не существует! Попробуй еще раз!")
        else:
            print(f"Город {city_input} не существует! Попробуй еще раз! Тебе на \"{last_liter.upper()}\"")
print("Ты победил!!!")

