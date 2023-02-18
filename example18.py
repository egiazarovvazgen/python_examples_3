"""
Требуется найти в массиве a[1 ... n] самый близкий по величине элемент к заданному числу x.
Пользователь в первой строке вводит натуральное число n - количество элементов в массиве.
В последующих строках записаны n целых чисел a[i]. Последняя строка содержит число x.
"""


def nearest(lst, target):
    return min(lst, key=lambda x: abs(x - target))


numbers = []
n = int(input("Введите количество чисел в списке: "))
for i in range(n):
    numbers.append(int(input("Введите число: ")))
print(f"Ваш список: {numbers}")
x = int(input("Введите некоторое число x: "))
print(f"Самый близкий по величине элемент к заданному числу x: {nearest(numbers, x)}")