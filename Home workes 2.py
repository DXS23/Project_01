cities = ['Москва', 'Рим', 'Париж']
population = [[150], [100], [110]]
print('Население ', cities[0], '-', *population[0], 'человек')
population = sum(population, [])
print('Итого размер населения - ', sum(population), 'человек')