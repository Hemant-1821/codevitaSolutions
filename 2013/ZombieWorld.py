try:
    B,N = input().split()
    B,N = int(B),int(N)
    li = list(map(int,input().split()))
except Exception:
    print("Invalid Input")
    exit(0)
bol = False
li.sort(reverse=True)
for i in li:
    B = B-((i%2)+(i/2))
if(B>0):
    print('YES')
else:
    print('NO')