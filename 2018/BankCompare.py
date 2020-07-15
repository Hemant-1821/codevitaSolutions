for i in range(int(input())):
    prin = int(input())
    years = int(input())
    slabs_a = int(input())
    #print(prin,years,slabs_a)
    sum_a = 0
    sum_b = 0
    for slab in range(slabs_a):
        yrs,mir = input().split()
        num = prin * float(mir)
        den = ( 1 - 1 / (1 + float(mir))**(float(yrs) * 12))
        sum_a += float(num/den)
    slabs_b = int(input())
    for slab in range(slabs_b):
        yrs,mir = input().split()
        num = prin * float(mir)
        den = ( 1 - 1 / (1 + float(mir))**(float(yrs) * 12))
        sum_b += float(num/den)
    if sum_a > sum_b:
        print('Bank B')
    else:
        print('Bank A')