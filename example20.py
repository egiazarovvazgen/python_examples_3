"""
Скрэббл. Каждая буква имеет определённую ценность. Напишите программу, которая вычисляет
стоимость введённого пользователем слова. Будем считать, что на вход подаётся только
одно слово, которое содержит либо только английские, либо только русские буквы.
"""

import re


def isRussian(word):
    return bool(re.search("[а-яА-Я]", word))


points_en = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10: "QZ"}
points_ru = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
word = input("Введите английское или русское слово: ").upper()
if isRussian(word):
    print(sum([k for i in word for k, v in points_ru.items() if i in v]))
else:
    print(sum([k for i in word for k, v in points_en.items() if i in v]))
