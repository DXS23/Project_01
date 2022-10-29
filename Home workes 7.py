
titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

for prod_name, prod_code in titles.items():
    for product in sales[prod_code]:
        total_quant = 0
        total_coast = 0
        quant = product['quantity']
        coast = product['price']
        total_quant += quant
        total_coast += coast * quant
        print(prod_name, '-', quant, 'шт, стоимость', total_coast, 'руб')



# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Отлично!
#  мой вариант был таким
item_of_goods = []

for product_name, product_code in titles.items():

    product_quantity = 0
    product_value = 0

    for position in sales[product_code]:
        product_quantity += position['quantity']
        product_value += position['quantity'] * position['price']

    print(product_name, '-', product_quantity, 'шт, стоимость', product_value, 'рублей')
