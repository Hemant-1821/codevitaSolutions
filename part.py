def check(arr, av):
    stack = []
    final = []
    i = 0
    while i < len(arr):
        stack.append(arr[i])
        if sum(stack) == av:
            #save
            print(stack)
            for h in stack:
                arr.remove(h)
            stack.clear()
            i = 0
        elif sum(stack) > av:
            stack.pop()
            i += 1
        else:
            i += 1

check([1,1,1,1,1,1], 2)
            
            