
# FoodSuggestV1.py
import random
with open(r'windproject\FoodSuggest\foodlist.csv', 'r', encoding='utf-8') as fo:
    f1 = fo.readline()
list1= f1.split(',')
flag = 'n'
while flag != 'y':
    suggest = random.choice(list1[1:])
    print(f'今天吃{suggest}好吗')
    flag = input('同意就输入y,否则重新随机推荐')
print(f'就决定是你了，{suggest}!')

