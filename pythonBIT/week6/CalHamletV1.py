# CalHamletV1.py
def getText():
    txt = open(r'pythonBIT\week6\hamlet.txt', 'r', encoding='utf-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}.~‘’':
        txt = txt.replace(ch, '')
    return txt

hamletTxT = getText()
words = hamletTxT.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(f'{word:<10}{count:>5}')

    
