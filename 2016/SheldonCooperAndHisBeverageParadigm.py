def check(array, num):
    array.sort()
    for i in range(len(array)-1):
        left = i+1
        right = len(array)-1
        while left<right:
            sums = array[left]+array[right]+array[i]
            if sums == num:
                return True
            elif sums < num:
                left += 1
            elif sums > num:
                right -= 1
    return False

li = []
N = int(input())
for _ in range(N+1):
    inp = li.append(int(input()))
    
print(check(li[:-1],li[-1]))