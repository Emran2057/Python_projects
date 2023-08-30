num = int(input("Enter number of row * in. "))
meth = bool(int(input("Enter 1 or 0: ")))

if meth is True:
    for i in range(0, num+1):
        st = "*"
        for j in range(0, i):
            print(st, end=' ')
        print("")


elif meth is False:
    for i in range(num+1, 0, -1):
        st = "*"
        for j in range(1, i+1):
            print(st, end=' ')
        print("")