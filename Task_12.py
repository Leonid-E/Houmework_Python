# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 44 -> 22
# 56 -> 23

S = int(input('Сумма чисел : '))
P = int(input('Произведение чисел : '))
conceived_numbers_1 = 0
conceived_numbers_2 = 0
for i in range(S): 
    difference = S - i 
    # print(f'{S} - {i} = {difference}')
    for i in range(1,P + 1):
        segmentation = int (P / i)
        if(P % i == 0):
            # print(f'{P} / {i} = {segmentation}' )
            if (difference + segmentation == S and segmentation * difference == P):
                conceived_numbers_1 = difference
                conceived_numbers_2 = segmentation  
print(f'{conceived_numbers_1}, {conceived_numbers_2}')
if(conceived_numbers_1 == 0 and conceived_numbers_2 == 0): 
    print('Некорректные числа')            
                
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
