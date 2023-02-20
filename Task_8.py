# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
length = int(input('Длина шоколадки : '))
width = int(input('Ширина шоколадки : '))
number_slices = int(input('Kоличество долек : '))
total = length * width  # всего долек

if (number_slices % width == 0 or number_slices % length == 0):
    print (F'-> yes')
else:
    print (F'-> no')
  