for _ in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))
    count = 0
    for i in li:
        if count < li.count(i):
            count = li.count(i)
        li.remove(i)
    print(count)
    