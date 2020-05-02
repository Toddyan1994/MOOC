# temp converter
# edit note: using the newest powerful f-formatting technique
tempstr = input("plz input temperature in C or F format:")
if tempstr[-1] in ['F', 'f']:
    C = (eval(tempstr[0:-1]) - 32) / 1.8
    print(f"converted temp is {C:.2f}C")
elif tempstr[-1] in ['C', 'c']:
    F = eval(tempstr[0:-1]) * 1.8 + 32
    print(f"converted temp is {F:.2f}F")
else:
    print("wrong input")
