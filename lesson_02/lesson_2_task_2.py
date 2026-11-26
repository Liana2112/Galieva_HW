year = int(input("Введите год в формате YYYY:"))

def is_year_leap(year):
    return True if year % 4 == 0 else False

result = is_year_leap(year)
print(f"Год {year}: {result}")