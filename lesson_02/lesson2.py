#Выведите на экран второй и второй с конца элементы через запятую. Продумайте такое решение, 
# которое можно было бы применить к списку любой длины.

employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
print(employee_list[1] + ', ' + employee_list[-2])

#Создайте функцию dev_by_three, которая принимает один аргумент — число — и возвращает 'Да', если оно делится на три, и 'Нет' — если не делится.
# В этом же файле напишите код, который вызывает функцию и передает в нее число.
# Результат вызова функции должен сохраняться в переменную.
# Выведите в консоль сообщение в формате: 
# Делится ли на три <число>? - Нет | Да

def dev_by_three(num):
    return "Да" if(num % 3 == 0) else "Нет"

num = int(input("Введите число:"))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")

import math
def min_boxes(items):
    return math.ceil(items / 5)

num_items = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(num_items)}")

num = int(input("Введите число: "))

def check_divisibility(num):
    for n in range(1, num + 1):
        if n % 4 == 0:
            print(f"{n} - Делится и на 2 и на 4")
        elif n%2 == 0:
            print(f"{n} - Делится на 2, но не на 4")
        else:
            print(n)

check_divisibility(num)          

def quarter_of_year(month):
    if month >= 1 and month <= 3:
        return "I квартал"
    if 4 <= month <= 6:
        return "II квартал"
    if 7 <= month <= 9:
        return "III квартал"
    if 10 <= month <= 12:
        return "IV квартал"
    else:
        return "Некорректный месяц"

month = int(input("Введите номер месяца от 1 до 12:"))
print (quarter_of_year(month))

lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
result = [x for x in lst if x % 3 == 0 and x > 15]
print(result)

my_list = list(range(25, 0, -5))
print(my_list)



var_1 = 50
var_2 = 5

temp = var_1
var_1 = var_2
var_2 = temp

print("var_1 =", var_1)
print("var_2 =", var_2)