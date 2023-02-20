# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

three_number  = int (input('Введите трёхзначное число : '))
first_number  = three_number // 100
second_number = three_number // 10 % 10
third_number  = three_number % 10
sum = first_number + second_number + third_number 
print (F'-> {sum} ({first_number} + {second_number} + {third_number})')
