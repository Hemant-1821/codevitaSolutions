for _ in range(int(input())):
    N = int(input())
    li = list(map(int,input().split()))
    ans = []
    start = 0
    while start < N-1:
        #print(start)
        temp = []
        temp = [li[start]]
        while start < N-1 and li[start+1] >= li[start]:
            temp.append(li[start+1])
            start += 1
        ans.append(temp)
        start += 1
    if len(ans) > 0:
        maxi = ans[0]
        for i in range(len(ans)):
            if len(maxi) < len(ans[i]):
                maxi = ans[i]
        for i in maxi:
            print(i,end=' ')
        print('')
    else:
        print(li[0])
            