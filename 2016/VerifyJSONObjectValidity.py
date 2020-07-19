import sys
JSON = input().strip()
stack = []
open_bkt = False
if JSON[0] == '{':
    starting_bkt = True
    flag = True
    stack.append('{')
    stack.append('S')
else:
    starting_bkt = False
    flag = False
JSON = JSON[1:]
try:
    for i in JSON:
        # print('past')
        if i == '{' and flag and starting_bkt:
            open_bkt = True 
            # print('appended',i)
            stack.append(i)
        elif i == '}' and (stack[-1] == '{' or stack[-1] == 'S') and flag:
            # print('poped',i)
            if stack[-1] == '{':
                stack.pop()
                open_bkt = False
            elif stack[-1] == 'S':
                stack.pop()
                stack.pop()
                starting_bkt = False
        elif i == ':' or i == ',' and flag and starting_bkt:
            continue
        elif i == '[' and flag and (open_bkt or starting_bkt):
            # print('appended',i)
            stack.append(i)
        elif i == ']' and stack[-1] == '[' and open_bkt == False and flag and starting_bkt:
            #print('poped',i)
            stack.pop()
            open_bkt = False
        else:
            flag = False
            break
except:
    print('-1')
    sys.exit(0)
    # print(stack[-1])
if flag and len(stack) == 0 and open_bkt == False and starting_bkt == False:
    print('1')
else:
    print('-1')


# {:[{},{}]}