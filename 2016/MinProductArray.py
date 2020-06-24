for _ in range(int(input())):
    N,K = input().split()
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))
    original_sum, new_sum = 0, 0
    for i in range(int(N)):
        original_sum += li1[i]*li2[i]
    new_sum = original_sum
    for i in range(int(N)):
        prev_prod = li1[i]*li2[i]
        new_prod = min((li1[i]-(2*int(K)))*li2[i],(li1[i]+(2*int(K)))*li2[i])

        temp_sum = original_sum - prev_prod + new_prod
        if temp_sum < new_sum:
            new_sum = temp_sum
    print(new_sum)