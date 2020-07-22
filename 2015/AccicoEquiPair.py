li = list(map(int,input().strip().split()))
a = 1
b = len(li) - 2
left_sum = li[0]
right_sum = li[-1]
flag = False
sums = sum(li) 
if len(li) > 4:
    while b > a+1:
        while li[a] == li[a+1] == 0:
            a += 1
        while li[b] == li[b-1] == 0:
            b -= 1

        middle = sums - left_sum - right_sum - li[a] - li[b]
        if left_sum == right_sum == middle:
            flag = True
            break
        if left_sum > middle or right_sum > middle:
            flag = False
            break

        if left_sum < right_sum:
            left_sum += li[a]
            a += 1
        elif left_sum > right_sum:
            right_sum += li[b]
            b -= 1
        else:
            if (left_sum + li[a]) == (middle - li[a+1]):
                left_sum += li[a]
                a += 1
            elif (right_sum + li[b]) == (middle - li[b-1]):
                right_sum += li[b]
                b -= 1
            else:
                left_sum += li[a]
                right_sum += li[b]
                b -= 1
                a += 1

    if flag:
        print('Indices which form equi pair { '+str(a)+','+str(b)+' }')
        print('Slices are { 0,'+str(a-1)+' },{ '+str(a+1)+','+str(b-1)+' },{ '+str(b+1)+','+str(len(li)-1)+' }')
    else:
        print('Array does not contain any equi pair')
else:
    print('Array does not contain any equi pair')