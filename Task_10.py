# Задача 10. На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

numbers_coins = int(input('Количество монет на столе : '))
numbers_reshka = 0
numbers_orel = 0
for i in range(numbers_coins): 
    from random import randint as RI
    coins = RI(0,1)
    if (coins == 1):
        reshka = coins   
        numbers_reshka += 1
        print(f'Решка', end=' ')
    else: 
        orel = coins 
        numbers_orel += 1
        print(f'Орёл', end=' ')
print ()
print (f'Mонеты с решкой = {numbers_reshka}')
print (f'Mонеты с орлом = {numbers_orel}')
if (numbers_reshka > numbers_orel):
    print(f'{numbers_reshka} > {numbers_orel} значит нужно перевернуть монеты с орлом')
if (numbers_reshka == numbers_orel):
    print(f'{numbers_reshka} = {numbers_orel} перевернуть можно любые монеты') 
else:
    print(f'{numbers_reshka} < {numbers_orel} значит нужно перевернуть монеты с решкой')