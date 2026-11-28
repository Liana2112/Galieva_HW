def month_to_season(month):
    if month == 12 or 1 <= month <= 2:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    else:
        return "Некорректный месяц"

month = int(input("Введите номер месяца от 1 до 12:"))
print (month_to_season(month))