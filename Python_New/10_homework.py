#10 Построение графиков
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random
import os
path = 'whoAmI'
basename = os.path.basename(path)


questions = ['robot', 'human']
mix_questions = [random.choice(questions) for i in range(10)]

data = pd.DataFrame({'whoAmI': mix_questions})

distinct_data = set(data['whoAmI'])

one_hot_view = pd.DataFrame()


for i in distinct_data:
    one_hot_view[i] = data['whoAmI'].apply(lambda x: 1 if x == i else 0) #.astype(int)

print ('\033[1m', basename, '\033[0m', '\n' , '____________')

print (one_hot_view.to_string(index = False))