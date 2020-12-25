def factors(n):
    fact = []
    for i in range(1,(n//2)+1):
        if n%i == 0:
            fact.append(i)
    return max(fact)

def cal_hcf(n1,n2):
    while(n2):
        n1, n2 = n2, n1 % n2
    return n1

def addition(li1,li2):
    li = list(set(li1) | set(li2))
    return li


n1, n2 = map(int,input().split())

#print(n1,n2)

if n1 == n2:
    print(str(0))
    
else:
    hcf = cal_hcf(n1,n2)
    li_n1 = [n1,factors(n1)]
    li_n2 = [n2,factors(n2)]
    while True:
        if li_n1[-1] == 1 and li_n2[-1] == 1:
            break
        else:
            if li_n1[-1] != 1:
                li_n1.append(factors(li_n1[-1]))
            if li_n2[-1] != 1:
                li_n2.append(factors(li_n2[-1]))
    
    li = addition(li_n1, li_n2)
    li2 = sorted(li_n2,reverse=False)
    print(li_n1,li2,hcf)
    count = 0
    for i in li:
        if i > hcf:
            count += 1
    
    print(count)
