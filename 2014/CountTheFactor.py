import math
import sys

def prime(n):
    flag = True
    li = []
    for i in range(2,n):
        flag = True
        for j in range(2,int(math.sqrt(i)+1)):
            if(i%j==0):
                flag = False
        if(flag):
            li.append(i)
    return li
            
try:
    num = int(input())
except:
    print('Invalid Input')
    sys.exit(1)

    
prime = prime(num)
count = [0]*len(prime)
for i in range(len(prime)):
    co = 0
    sq = prime[i]
    while(1):
        co = co + num//sq
        sq = sq*prime[i]
        #print(sq)
        if(sq>num):
            break
    count[i] = co
        
        
count.sort(reverse=True)
if 0 in count:
    for _ in range(count.count(0)):
        count.remove(0)
for i in count:
    print(i,end=' ')
    

