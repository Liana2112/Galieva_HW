import math

def square(num):
    return num * num

num = math.ceil(float(input("Введите сторону квадрата:")))
print(f"Площадь квадрата со сторонами {num} равна {square(num)}")