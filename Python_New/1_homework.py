# №1
#Задание_1 n = 123
# res = (n//10)//10 + (n//10)%10 + n%10

#Задание_2 n = 6
# print(f'{round((n-(n/3)*2)/2)} {round((n/3)*2)} {round((n-(n/3)*2)/2)}')

#Задание_3 n = 385916
# if ((((((n//10)//10)//10)//10)//10)%10 + ((((n//10)//10)//10)//10)%10 + (((n//10)//10)//10)%10) == (((n//10)//10)%10 + (n//10)%10 + n%10):
#     print('yes')
# else:
#     print('no')

#Задание_4 a = 3; b = 2; c = 4
# if  c < a * b and c % a == 0 or c % b == 0 :
#     print(f'yes')
# else :
#     print(f'no')

# №2
#Задание_1 coins = [0, 1, 0, 1, 1, 0]
# gerb = 0
# reshka = 0
# for i in coins:
#     if i == 1:
#         gerb += 1
#     else:
#         reshka += 1
# print (gerb if gerb < reshka else reshka)

#Задание_2 s = 12; p = 27
# x, y = 1, 1
# for x in range (1, 1001) :
#     y = s - x 
#     if x <= y and x * y == p : 
#         print (x,y, end=' ')

#Задание_3 n=16
# k = 0
# res = 1
# while res <= n: 
#     print(res)
#     k += 1
#     res = 2 **k

# №3
#Задание_1 list_1 = [1, 2, 3, 4, 5]
#k = 3
# res = []
# for i in list_1: 
#     if i == k:
#         res.append (k)
#         i +=1
# print(len(res))

#Задание_2 list_1 = [1, 2, 3, 4, 5]
# k = 6
# list_1.sort()
# res = list_1[0]
# for n in list_1:
#         if abs(n - k) < abs(res - k):
#             res = n
#         if n > k:
#             break
# print (res)

#Задание_3 k = 'ноутбук'
# res_rus_eng = {1:'АВЕИНОРСТAEIOULNSTR', 2:'ДКЛМПУDG', 3:'БГЁЬЯBCMP', 4:'ЙЫFHVWY', 5:'ЖЗХЦЧK', 8:'ШЭЮJX', 10:'ФЩЪQZ'}
# k = k.upper()
# sum = 0
# for i in k: 
#     for j, log in res_rus_eng.items():
#         if i in log:
#             sum += j
# print(sum)

# №4
#Задание_1 var1 = '5 4' 
#var2 = '1 3 5 7 9' 
#var3 = '2 3 4 5' 
# var2_num = [int(x) for x in var2.split()]
# var3_num  = [int(x) for x in var3.split()]
# var1 = (var2_num  + var3_num )
# res = list ()
# for i in set (var1):
#     if var1.count(i) > 1:
#         res.append (i)
# res.sort()
# print(*res)

#Задание_2 arr = [5, 8, 6, 4, 9, 2, 7, 3]
# arr_2 = []
# for i in range (len(arr)):
#     arr_2.append(arr[i]+arr[i-1]+arr[i-2])
# max_number = arr_2[0]
# for k in arr_2:
#     if max_number < k:
#         max_number = k
#         k +=1
# print(max_number)


# №5
#Задание_1 
#def sum(a, b):
#     if a == 0:
#         return a + b
#     else:
#         return sum (a-1, b+1)

#a = 3
#b = 5
#print(f(a, b))

#Задание_2
#  def sum(a, b):
#     if a == 0:
#         return a + b
#     else:
#         return sum (a-1, b+1)

# a = 2
# b = 2
# print(sum(a, b))

# №6
#Задание_1 list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#min_number = 0
#max_number = 10
# def ind_res (min_number, max_number):     
#     list_2 = []
#     for i in range(len(list_1)):
#         if max_number >= list_1[i] >= min_number:
#                 list_2.append(i)
#     return list_2 
# print (*ind_res(min_number, max_number), sep = "\n")

#Задание_2 a1 = 2; d = 3; n = 4
# def a_pr (a1, d, n):
#     massive = []
#     for i in range (n):
#         massive.append(a1 + i * d)        
#     return massive

# print (*a_pr(a1, d, n), sep = '\n') 

# №7
#Задание_1
def print_operation_table(operation, num_rows = 9, num_columns = 9):
	if num_rows < 2 or num_columns < 2:
		print('ОШИБКА! Размерности таблицы должны быть больше 2!')
	else:
		print(' '.join([str(i) for i in range(1, num_columns + 1)]))
		for i in range(2, num_rows + 1):
			print(i, end = ' ')
			for j in range(2, num_columns + 1):
				print(f'{operation(i, j)} ')
			print()


print_operation_table(lambda x, y: x * y, 3, 3)

#Задание_2
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

def count (spisok):
    glasnye = 'аеиоуыэюя'
    count = 0    
    for x in spisok:
        if x in glasnye:
            count += 1
    return count


words = stroka.split(' ')
if len(words) <= 1:
    n_phrases = len(words)
    print('Количество фраз должно быть больше одной!')
else:
    spisok = list(map(lambda i: i.replace('-',''), words)) #['парарарам', 'рампампапам', 'парападам']
    res = ([count(i) for i in spisok])
    if len(set (res)) ==1 :
        print("Парам пам-пам")
    else:
        print("Пам парам") 