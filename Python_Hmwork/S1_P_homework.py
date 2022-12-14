# <!-- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет -->

print ('Input N of day of a week =')
N = int (input())
counter = 0
while N in range (-100,100) and counter <1 :
    if N > 5 and  N < 8: 
        counter +=1
        print ('Yes, It\'s weekend')
    elif N <= 5 and N > 0:
        counter +=1
        print ('No, It\'s working day')
    else:
        counter +=1
        print ('Error input! Input numbers from 1 to 7')

# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# f[x]  с^2 = a^2 + b^2
# distance = sqrt((xb - xa)^2 + (yb - yb)^2)
# в python нет операнда для извлечения корня - хитрость - степень 0.5
AX_point = float(input('Input А point\'s coordinate on axis Х: '))
AY_point = float(input('Input А point\'s coordinate on axis Y: '))
BX_point = float(input('Input B point\'s coordinate on axis Х: '))
BY_point = float(input('Input B point\'s coordinate on axis Y: '))
distance = round(((BX_point - AX_point)**2 + (BY_point - AY_point)**2)**0.5,2)
print(distance)