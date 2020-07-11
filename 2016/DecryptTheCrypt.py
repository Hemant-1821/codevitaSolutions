import sys
def isUniq(st):
    li = list(st)
    i = 0
    while len(li) > 1:
        temp = li[i]
        li.remove(li[i])
        if temp in li:
            return False
        else:
            continue
    return True

for _ in range(int(input())):
    N1 = input()
    char = input()
    try:
        li = list(map(str,N1.split('||')))
        #print(li)
        li1 = list(map(str,li[0].split('|')))
        C = li1
        B = li[1][0:(len(li[-1])-1)]
        A = int(li[1][-1])
        if isUniq(char) and len(li1) == 10 and len(li) == 2 and len(char) == 10:
            #print(B,C,A)
            di = {}
            for i in C:
                if len(i) > 1:
                    for j in range(0,len(i) - 1):
                        di[int(i[j])] = int(i[-1])
            #print(di)
            for i in B:
                di[int(i)] = di[int(i)] + 10

            #print(di)

            fin = []
            for i in range(0,len(di)):
                fin.append(di[i])

            fin[-1] = fin[-1] - A

            for i in reversed(range(1,len(fin))):
                fin[i-1] = abs(fin[i] - fin[i-1])

            pwd = ''
            for i in fin:
                pwd = pwd + char[i]
            print(pwd)
        else:
            sys.exit()
    except:
        print('-1')