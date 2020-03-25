T = int(input())
for _ in range(T):
    inp = int(input())
    moves = inp//4 + inp%4
    if(moves%2==0):
        print('No')
    else:
        print('Yes')