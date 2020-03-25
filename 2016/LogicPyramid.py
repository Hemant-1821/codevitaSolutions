def element(count):
    first = 6
    second = 28
    if count == 1:
        return first
    elif count == 2:
        return second
    else:
        count = count-2
        for h in range(0,count):
            next_ele = (second*2)-first+16
            first = second
            second = next_ele
    return next_ele
N = int(input())
for t in range(N):
    inpp = int(input())
    count = 1
    for i in range(1,inpp+1):
        for j in range((inpp-i)*3):
            print(' ',end='')
        for k in range(0,i):
                print(format(element(count),'05'),end='')
                print(' ',end='')
                count = count + 1
        print('')