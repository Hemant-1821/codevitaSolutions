import math
def prime_1(n):
    prime_li = []
    for i in range(2,n):
        flag = True
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                flag = False
                break
        if(flag):
            prime_li.append(i)
    return prime_li
T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    prime = prime_1(n)
    if(len(prime)>0):
        for i in range(1,len(prime)):
            sum_n = 0
            for j in range(0,i):
                sum_n = sum_n + prime[j]
                if sum_n == prime[i]:
                    count = count+1
                    break
                elif sum_n > prime[i]:
                    break
        print(count)
    else:
        print('0')
