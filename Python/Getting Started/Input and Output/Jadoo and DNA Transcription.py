l = ""
flag = True
for i in input():
    if i == "G":
        l = l + "C"
    elif i == "C":
        l = l + "G"
    elif i == "T":
        l = l + "A"
    elif i == "A":
        l = l + "U"
    else:
        flag = False
if flag:
    print(l)
else:
    print("Invalid Input")