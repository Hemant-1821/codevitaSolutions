import math

def isPrime(n):
    if n == 1 or n==0: 
        return False
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True

def isHappy(n):
    if(n==1):
        return False
    n_sum = 0
    while n>0:
        n_sum=n_sum + ((n%10)*(n%10))
        n = n//10
    if n_sum==1:
        return True
    elif(n_sum==4):
        return False
    return isHappy(n_sum)

def main():
    try:
        X = int(input())
        Y = int(input())
        N = int(input())
        if(X<0 and Y<0 and Z<0):
            print('Invalid Input')
            exit(0)
        count = 0
        for i in range(X,Y+1):
            if(isPrime(i)):
                if(isHappy(i)):
                    count=count + 1
                    if(count==N):
                        print(i)
                        break
        if(count!=N):
            print('No number is present at this index')
    except Exception:
        print('Invalid Input')

main()
 
