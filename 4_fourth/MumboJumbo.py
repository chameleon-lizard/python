a = []
b = []
oddity = 0
string = input()
while string != "":
    for i in string:
        if not oddity:
            if not i in a:
                a.append(i)
        else:
            if not i in b:
                b.append(i)
    string = input()
    oddity += 1
    oddity %= 2
                
if a.__len__() > b.__len__():
    print("Mumbo")
else:
    print("Jumbo")
