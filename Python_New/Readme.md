## <font color=#00ff > **Homework  for new Python course** </font>

***file 1_homework.py содержит ДЗ 1 - 7 семинара***

***pull request - это выполнение ДЗ 8 семинара***  

***file 9_homework.py содержит ДЗ 9 семинара***

***file 10_homework.py содержит ДЗ 10 семинара***

## <font color=#00ffff > **ДЗ №1.** </font>
#### Задание_1: Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.

Пример:n = 123 -> res = 6 (1 + 2 + 3), n = 100 -> res = 1 (1 + 0 + 0)

#### Задание_2: Журавлики
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

Пример: n = 6 -> 1 4 1  
n = 24 -> 4 16 4    
n = 60 -> 10 40 10 

#### Задание_3: Счастливый билет
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

Пример: n = 385916 -> yes
n = 123456 -> no

#### Задание_4: Шоколадка
Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.

Пример: a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no

## <font color=#00ffff > **ДЗ №2.** </font>
#### Задание_1: Монетки
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
Входные данные:
На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
Выходные данные:
Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
Пример использования На входе:
coins = [0, 1, 0, 1, 1, 0]

#### Задание_2: Петя и Катя
– брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

Пример На входе: s = 12, p = 27
На выходе: 3 9

#### Задание_3: Целые степени двойки
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

Пример n=16
Вывод
1
2
4
8
16

## <font color=#00ffff > **ДЗ №3.** </font>
#### Задание_1: Встречаемость элемента в массиве
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.

Пример: list_1 = [1, 2, 3, 4, 5] k = 3
Ответ: 1

Задание_2: Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример: list_1 = [1, 2, 3, 4, 5] k = 6
Ответ: 5

Задание_3: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример: k = 'ноутбук'
Ответ: 12

## <font color=#00ffff > **ДЗ №4.** </font>
#### Задание_1: Сравнение числовых списков
Даны два неупорядоченных набора целых чисел (возможно с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m / n - кол-во элементов первого множества. / m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример На входе: var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе: 
3 5

#### Задание_2: Сбор черники
В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.
Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.
В фермерском хозяйстве внедрена система авто сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
Ваша задача - написать программу, которая определит макс число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

Входные данные: На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.
Выходные данные: Программа должна вывести одно целое число - макс количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

Пример использования На входе: arr = [5, 8, 6, 4, 9, 2, 7, 3]

## <font color=#00ffff > **ДЗ №5.** </font>
#### Задание_1: Возведение в степень
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.

Пример: a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 

#### Задание_2:  Рекурсия
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.

Пример: sum(2, 2)
Ответ: 4

## <font color=#00ffff > **ДЗ №6.** </font>
#### Задание_1: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

Пример На входе: list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 3
На выходе: 
1
2
3

#### Задание_2: Арифметическая прогрессия
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

Пример На входе: a1 = 2; d = 3; n = 4
На выходе:
2
5
8
11

## <font color=#00ffff > **ДЗ №7.** </font>
#### Задание_1: Функции
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Пример На входе: print_operation_table(lambda x, y: x * y, 3, 3)
На выходе:
1 2 3
2 4 6 
3 6 9

#### Задание_2: Стихи Винни-Пуха
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

Пример На входе: stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
На выходе: Парам пам-пам

## <font color=#00ffff > **ДЗ №8.**  </font>
#### Работа с файлами:
Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

Формат сдачи: ссылка на свой репозиторий или pull request.

## <font color=#00ffff > **ДЗ №9.** </font>
Задание_1: Определить среднюю стоимость дома:
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.

#### Задание_2: Максимальное значение households:
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.

## <font color=#00ffff > **ДЗ №10.** </font>
#### Задача 44: Перевод в One Hot вид
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

Формат сдачи: ссылка на свой репозиторий.
