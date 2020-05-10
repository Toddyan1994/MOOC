# open2.py
with open(r'windproject\IO\txtfile\scores.txt',
          'r', encoding='utf-8') as file1:
    lines1 = file1.readlines()
    print(lines1)

lines2 = open(r'windproject\IO\txtfile\scores.txt',  # 只操作1次时更省力的办法
           'r', encoding='utf-8').readlines()
print(lines2)

final_scores = []

for i in lines2:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = data[0]+str(sum)+'\n'
    final_scores.append(result)

with open(r'windproject\IO\txtfile\winner.txt',
          'w', encoding='utf-8') as new1:
    new1.writelines(final_scores)
