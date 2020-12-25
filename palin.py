n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
count = 0

def isPal(temp):
    l = 0
    r = len(temp)-1
    while l < r:
        if temp[l] != temp[r]:
            return False
        l += 1
        r -= 1
    return True

for i in range(n1,n2+1):
    for j in range(0,24):
        for k in range(0,60):
            for l in range(0,60):
                temp = str(i) + str(format(j, '02'))+str(format(k, '02'))+str(format(l, '02'))
                if isPal(temp):
                    print(temp)
                    count += 1
print(count)