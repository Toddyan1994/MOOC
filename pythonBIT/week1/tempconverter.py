#temp converter
tempstr=input("plz input temperature in C or F format:")
if tempstr[-1] in ['F','f']:
    C=(eval(tempstr[0:-1])-32)/1.8
    print("converted temp is {:.2f}C".format(C))
elif tempstr[-1] in ['C','c']:
    F=eval(tempstr[0:-1])*1.8+32
    print("converted temp is {:.2f}F".format(F))
else:
    print("wrong input")