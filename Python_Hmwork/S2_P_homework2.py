# 1.(https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=33&id_problem=190)
# Монетки
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток. 
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.
print ('Task 1')
import random
coin_up = 0
coin_down = 0
order = list()
for i in range(10):
    order.append(random.randint(0 , 1)) #range of random between 2 numbers
print(order)
for i in order:
    if i == 0:
        coin_up += 1
    else:
        coin_down += 1
min_try = 0 #we can also use built-in function "min" in print
if coin_up < coin_down:
        min_try = coin_up
else:
        min_try = coin_down  
print('Minimum N of try is:', min_try)

# 2.(https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=33&id_problem=197)
# Сумма
# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
# Входные данные
# В единственной строке входного файла INPUT.TXT записано единственное целое число N, 
# не превышающее по абсолютной величине 10 в 4 степени.
print ('Task 2')
m = int (input('Enter a first number: '))
n = int (input('Enter a second number: '))
print (sum(range(m, n + 1)))

# 3.(https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=34&id_problem=205)
# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

print ('Task 3')
n = int(input('Input Your Number: '))
counter = 0
min_divisor = 0
for i in range(2, n + 1):
        if n % i == 0:
                n = i
                print ('Your Number min divsor is: ', n)
     
# 4.(https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=699)
# Шеренга
# Петя впервые пришел на урок физкультуры в новой школе. 
# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, 
# если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.
# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). 
# Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. 
# Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.
print ('Task 4')
all_heights = [int(s) for s in input('Input heights of all people ≤ 200, use space button: ').split()] # список всех ростов через пробел
height_P = int(input('Input P height ≤ 200: '))     # рост Пети
position_P = len(all_heights) +1              #Петя становится правее более высокого (шеренга по убыванию роста)
print (all_heights)                           # Присваиваем переменой index длину списка а + 1
for i in range(len(all_heights)):             # список всех ростов без Пети
    if height_P > all_heights[i]:                     
        position_P = i +1                  
print('P is now № in sherenga: ', position_P)                    