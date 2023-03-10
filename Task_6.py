# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number_ticket  = int(input('Введите шестизначный номер билета : '))
left_side = number_ticket // 1000
right_side = number_ticket % 1000
sum_left_side = left_side // 100 + left_side % 100 // 10 + left_side % 10 
sum_right_side = right_side // 100 + right_side % 100 // 10 + right_side % 10 
if (sum_left_side == sum_right_side ):
    print (F'-> yes')
else: 
    print (F'-> no')
   