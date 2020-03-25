def part(start_row,end_row,n):
    for i in range(start_row,end_row+1):
        #start
        for j in range((n+1)-i):
            print(' ',end='')
        for k in range((2*i)-1):
            print('*',end='')
        print('')

T = int(input())
for h in range(0,T):
    n = int(input())
    if(n<=1):
        print("You cannot generate christmas tree")
    elif(n>20):
        print('Tree is no more')
    else:
        part(1,n+1,n)
        for x in reversed(range(2,n)):
            part(2,x+1,n)
        for _ in range(0,2):
            for i in range(0,n):
                print(' ',end='')
            print('*')