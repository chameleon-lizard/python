a = input()
b = {}

while a and a !=".":
    if a[0] == "#":
        a = input()
        continue
    
    if a.__contains__("="):
        try:
            right = a[:a.find("=")]
            exec(a, b)
        except Exception:
            if right.isidentifier():
                print("invalid assignment '" + a + "'")
            else:
                print("invalid identifier '" + right + "'")
    else:
        try:
            print(eval(a, b))
        except Exception as err:
            print(str(err))
    
    a = input()