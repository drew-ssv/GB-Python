# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет -->
print ('Task 1')
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

# 2.Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# f[x]  с^2 = a^2 + b^2
# distance = sqrt((xb - xa)^2 + (yb - yb)^2)
# в python нет операнда для извлечения корня - хитрость - степень 0.5
print ('Task 2')
AX_point = float(input('Input А point\'s coordinate on axis Х: '))
AY_point = float(input('Input А point\'s coordinate on axis Y: '))
BX_point = float(input('Input B point\'s coordinate on axis Х: '))
BY_point = float(input('Input B point\'s coordinate on axis Y: '))
distance = round(((BX_point - AX_point)**2 + (BY_point - AY_point)**2)**0.5,2)
print(distance)

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# РЕШЕНИЕ: Нумерация координатных плоскостей ведется против часовой стрелки римскими цифрами I, II, III, IV. 
# Если точка имеет "+" координату х (х > 0) и "+" координату у (у > 0), то она лежит в I четверти,
# "-" координату x (x < 0) и "+" координату у (у > 0), то она лежит в II четверти,
# "-" координату x (x < 0) и "-" координату у (у < 0), то она лежит в III четверти,
# "+" координату x (x > 0) и "-" координату у (у < 0), то она лежит в IV четверти.
print ('Task 3')
X_axis_coord = float(input('Input Your point\'s coordinate on axis Х: '))
Y_axis_coord = float(input('Input Your point\'s coordinate on axis Y: '))
if X_axis_coord == 0 and Y_axis_coord == 0:
    print("Your point is on the cross of X,Y axes")
elif X_axis_coord == 0 or Y_axis_coord == 0:
    print("Your point is on X,Y axes")
elif X_axis_coord > 0 and Y_axis_coord > 0:
    print("Your point is in a I quarter")
elif X_axis_coord < 0 and Y_axis_coord > 0:
    print("Your point is in a II quarter")
elif X_axis_coord < 0 and Y_axis_coord < 0:
    print("Your point is in a III quarter")
elif X_axis_coord > 0 and Y_axis_coord < 0:
    print("Your point is in a IV quarter")