# Задание_1: Определить среднюю стоимость дома
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома, 
# где количество людей от 0 до 500 (population) и сохранить ее в переменную avg. Используйте модуль pandas.

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] < df['median_house_value'].min()) & (df['population'] < 500)] ['median_house_value'].mean()


# Задание_2: Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" 
# и сохраните это значение в переменную max_households_in_min_population. Используйте модуль pandas.

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
max_households_in_min_population = df[df['population'] == df['population'].min()].households.max()