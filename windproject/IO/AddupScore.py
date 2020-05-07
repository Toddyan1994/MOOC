# open2.py
with open(r'D:\edu\MOOC\windproject\IO\txtfile\scores.txt','r',encoding='utf-8') as file1:
    lines=file1.readlines()
    print(lines)

final_scores=[]
for i in lines:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum+=int(score)
    result=data[0]+str(sum)+'\n'
    final_scores.append(result)

with open(r'D:\edu\MOOC\windproject\IO\txtfile\winner.txt','w',encoding='utf-8') as new1:
    new1.writelines(final_scores)