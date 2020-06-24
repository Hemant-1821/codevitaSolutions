for _ in range(int(input())):
    li = list(map(str,input().split()))
    i = 0
    names,numbers = [],[]
    while i<len(li):
        names.append(li[i].lower())
        numbers.append(int(li[i+1]))
        i += 2
    names = sorted(names)
    numbers.sort()
    for i in range(len(names)):
        print(names[i],numbers[i],end=' ')
    print('')