import sys
li = input()
N = int(input())
ptr = 0
first = []
for _ in range(N):
    tmp = list(input())
    if tmp[0] == 'L':
        ptr += int(tmp[2])
    elif tmp[0] == 'R':
        ptr -= int(tmp[2])
        
    if ptr >= 0:
        first.append(li[ptr])
    elif ptr < 0:
        first.append(li[ptr-1])
first = sorted(('').join(first))
for i in range(len(li)-N):
    if sorted(('').join(li[i:(i+N)])) == first:
        print('YES')
        sys.exit(0)
print('NO')