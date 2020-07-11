import math
def prime_li(N,M):
    li = []
    flag = True
    for i in range(N,M+1):
        flag = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                flag = False
        if flag:
            li.append(i)
    return li

def isPrime(N):
    for j in range(2,int(math.sqrt(N))+1):
        if N % j == 0:
            return False
    return True
for _ in range(int(input())):
    N = list(map(int,input().split()))
    if 2 <= N[0] <= 100 and 2 <= N[1] <= 100 and N[1] - N[0] >= 35:
        prime_list = prime_li(N[0],N[1])
        #print(prime_list)
        comb_li = []
        for i in prime_list:
            for j in prime_list:
                if i == j:
                    continue
                else:
                    comb_li.append(int(str(i)+str(j)))

        comb_li = set(comb_li)
        comb_prime = []
        for i in comb_li:
            if isPrime(i):
                comb_prime.append(i)

        comb_prime.sort()
        #print('comb_prime',len(comb_prime))

        small = comb_prime[0]
        large = comb_prime[-1]

        for _ in range(len(comb_prime)-2):
            sums = small+large
            small = large
            large = sums
        print(str(large))
