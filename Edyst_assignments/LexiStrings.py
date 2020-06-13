for _ in range(int(input())):
    alpha = input()
    string = input()
    li = []
    for i in string:
        li.append(alpha.index(i))
    li.sort()
    for i in li:
        print(alpha[i],end='')
    print('')