from queue import PriorityQueue
for _ in range(int(input())):
    N = int(input())
    li = list(map(int,input().strip().split()))
    pq = PriorityQueue()
    for i in li:
        pq.put(i)
    sums = 0
    while pq.qsize() != 1:
        sums_temp = pq.get()+pq.get()
        sums += sums_temp
        pq.put(sums_temp)
    print(sums)