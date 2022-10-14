user_input = input("Введите номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
1 <= month <= 12
if month == 2:
    print('28')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30')
else:
    print('31')
    if  month < 1 or month > 12:
        print('Номер месяца некорректен')