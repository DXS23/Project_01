salary, expenses = 10000, 12000
salary *= 12   #зарплата за 12 месяцев
sp = [12000]   # список с январём
for i in range(2,13):
    expenses += expenses * 0.03    # увеличение расхода каждый месяц от уже увеличенных расходов
    sp.append(expenses)
credit = sum(sp) - salary     # разница зарлаты и расходов за год
print('Необходимо взять в долг', round(credit, 2), 'рублей')
