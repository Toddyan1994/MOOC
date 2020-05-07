#modify poem.py
with open(r'windproject\IO\txtfile\poem1.txt', 'r', encoding='utf-8') as file1:
    lines=file1.readlines()
print(lines)  # 将读取到的内容打印出来，发现实际上读到的是带换行符的字符串。

line0='______________\n'
with open(r'windproject\IO\txtfile\poem1.txt','w', encoding='utf-8') as new: 
    for line in lines:  # 在内存中，对数据进行处理，然后再写到文档里，覆盖之前的内容。
        if line not in ['一弦一柱思华年。\n','只是当时已惘然。\n']:  # 注意：这里的条件要根据上面打印出的数据写。
            new.write(line)
        else:
            new.write(line0)            

# 请你根据学到的新知识，在下面完成对文档“poem1.txt”的修改。
# 你可以处理命名为“poem1”的文档，参考代码会处理“poem1.txt”。
