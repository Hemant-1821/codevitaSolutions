T = int(input())
for _ in range(T):
    li = list(map(int,input().split()))
    count = 0
    diff = li[1] - li[0]
    sum_li = li[1] + li[0]
    sum_dist = 0
    sum_diff = li[3]-li[1]
    while(not(sum_dist>=sum_diff)):
        sum_dist = sum_dist+diff
        count = count+1
    add_li = li[3]-sum_dist
    meters = (sum_li*count)+add_li
    print(meters*li[2])