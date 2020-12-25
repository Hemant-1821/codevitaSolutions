N = int(input())
li = list(map(int,input().split()))
li.sort()
#print(N,li)
ways = [0]*(N+1)

ways[li[0]] = 1
ways[li[1]] = 1
ways[li[2]] = 1
prime = 10**9 + 7
for i in range(li[0],N+1):
    for j in li:
        if i-j >= 0:
            ways[i] = (ways[i] + ways[i-j])%prime
print(ways[N])