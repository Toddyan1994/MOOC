# CalThreeKingdomsV2.py
import jieba

txt = open(r'pythonBIT\week6\threekingdoms.txt', 'r', encoding='utf-8').read()
excludes = {'将军', '却说', '二人', '荆州', '不可', '不能', '如此', '商议', '如何', '主公', '军士'}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word in ['诸葛亮', '孔明曰']:
        rword = '孔明'
    elif word in ['关公', '云长']:
        rword = '关羽'
    else:
        rword = word
        counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print(f'{word:<10}{count:>5}')
