alpha = list('abcdefghijklmnopqrstuvwxyz')
for _ in range(int(input())):
    inp = input()
    inp = inp[:-1]
    flag = True
    for i in inp:
        if inp.count(i) != (alpha.index(i))+1:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')