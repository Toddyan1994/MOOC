# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。

file1 = open(r'windproject\IO\txtfile\winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()

dict_scores = {}
list_scores = []
final_scores = []
for i in file_lines:
    data=i.split()
    data_name=data[0][:-3]  # 名字
    data_score=data[0][-3:]  # 分數
    dict_scores[data_score]=data_name 
    list_scores.append(data_score) 
list_scores.sort(reverse=True)
for i in list_scores:
    final_scores.append(f'{dict_scores[i]}{i}\n')

with open(r'windproject\IO\txtfile\winner.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(final_scores)
