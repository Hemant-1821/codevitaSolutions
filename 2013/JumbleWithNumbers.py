try:
    li = list(map(int,input().split()))
except Exception:
    print('Invalid Input')
    exit(0)
mathew = []
john = []
ma,jo,i = 0,0,0
while(1):
    ma = i*(2*i-1)
    if(ma>=li[1]):
        break
    mathew.append(ma)
    i = i+1
i=0
while(1):
    jo = i*(i+1)//2
    if(jo>=li[1]):
        break
    john.append(jo)
    i = i+1
m,j = 0,0
for _ in range(0,len(mathew)):
    if(mathew[_]>=li[0]):
        m = _
        break
for _ in range(0,len(john)):
    if(john[_]>=li[0]):
        j = _
        break
mathew = mathew[m:]
john = john[j:]
mathew = set(mathew)
john = set(john)
inter = sorted(mathew.intersection(john),reverse=False)
try:
    print(inter[li[2]-1])
except Exception:
    print("No number is present at this index")