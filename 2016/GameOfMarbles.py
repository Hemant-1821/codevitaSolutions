import math
import sys

def GCD(a,b,origa,origb):
    if a%b == 0:
        return int(int(origa*origb)/int(b)) 
    else:
        return GCD(b,a%b,origa,origb)

def LCM(N):
    a = N[0]
    b = N[1]
    li = GCD(a,b,a,b)
    for i in range(2, len(N)):
        li = GCD(li,N[i],li,N[i])
    return li

def check(li,guess):
    if LCM(li) == guess:
        return True
    else:
        return False

sal = 0
dar = 0
First = ''
Second = ''
h = int(input())
for _ in range(h//2):
    ques = list(input().split())
    ans = list(input().split())
    try:
        li = list(map(int,ques[1].split(',')))
        if 2<=len(li)<=7 and 1<=max(li)<=100:
            if(ques[0] == 'Sally'):
                if _ == 0:
                    First = 'Sally'
                    Second = 'Darrell'
                print("Sally's question is : {}".format(ques[1]))
                if ans[2] == 'PASS':
                    print('Question is PASSed')
                    print('Answer is: {}'.format(LCM(li)))
                    print('Darrell: 0points')
                else:
                    if check(li,int(ans[2])):
                        print('Correct Answer')
                        dar = dar+10
                        print('Darrell: 10points')
                    else:
                        print('Incorrect Answer')
                        print('Darrell: 0points')
            elif(ques[0] == 'Darrell'):
                if _ == 0:
                    First = 'Darrell'
                    Second = 'Sally'
                print("Darrell's question is : {}".format(ques[1]))
                if ans[2] == 'PASS':
                    print('Question is PASSed')
                    print('Answer is: {}'.format(LCM(li)))
                    print('Sally: 0points')
                else:
                    if check(li,int(ans[2])):
                        print('Correct Answer')
                        sal = sal+10
                        print('Sally: 10points')
                    else:
                        print('Incorrect Answer')
                        print('Sally: 0points')
        else:
            sys.exit()
            
        if _ == (h//2)-1:
            print('Total Points:')
            if First == 'Darrell':
                print('{}: {}points'.format(First,dar))
                print('{}: {}points'.format(Second,sal))
            else:
                print('{}: {}points'.format(First,sal))
                print('{}: {}points'.format(Second,dar))
            if(dar>sal):
                win = 'Darrell is winner'
            elif dar == sal:
                win = 'Draw'
            else:
                win = 'Sally is winner'
            print('Game Result: {}'.format(win))
    except:
        print('Invalid Input')
        break
