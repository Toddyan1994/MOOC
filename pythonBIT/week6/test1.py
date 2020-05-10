#test1.py
with open(r'pythonBIT\week6\hamlet.txt', 'r', encoding='utf-8') as fo:
    i=0
    for line in fo:
        print(line)
        i += 1
        if i > 20:
            break
