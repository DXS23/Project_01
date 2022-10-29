salary, expenses = 10000, 12000
salary *= 12   #зарплата за 12 месяцев
sp = [12000]   # список с январём
for i in range(2,12):
    expenses += expenses * 0.03    # увеличение расхода каждый месяц от уже увеличенных расходов
    sp.append(expenses)
credit = sum(sp) - salary     # разница зарлаты и расходов за год
print('Необходимо взять в долг', round(credit, 2), 'рублей')

# Траты растут ежемесячно по три процента от предыдущей суммы месяца.
# Поэтому реализация выглядит так

salary, expenses = 10000, 12000
i = 0
months_expenses = 0
money_needs = 0

while i < 12:

    if i == 0:
        months_expenses = expenses
    elif i >= 1:
        months_expenses *= 1.03
    i += 1
    difference = round(months_expenses-salary, 2)
    money_needs += difference
    print('Расходы в', i, 'месяце:', difference, ', Итого за', i, 'мес.:', round(money_needs,2))

print('Сотруднику необходимо взять', round(money_needs,2), 'рублей')
