string = input()
stack = []
flag = True
balanced = 0
stars = 0
start = '{(['
end = '})]'
pair = {
    '}':'{',
    ')':'(',
    ']':'['
}
for i in string:
    #print(i)
    if i in start:
        stack.append(i)
        #print(stars)
    elif i == '*':
        stack.append(i)
    elif (i in end) and len(stack) > 0:
        try:
            if stack[-1] == '*':
                while stack[-1] == '*':
                    temp = stack.pop()
                    stars += 1
            if stars >= 2:
                if len(stack) > 0:
                    if stack[-1] == pair[i]:
                        # if len(stack) > 0:
                        balanced += 1
                        stack.pop()  
                        # print(balanced)
                    else:
                        flag = False
                    #print(stars)   
                else:
                    flag = False
                    continue
            else:
                stack.pop()
                flag = False
                stars = 0
            if len(stack) == 0:
                stars = 0
        except:
            flag = False
            continue
    else:
        continue
if len(stack) != 0:
    for i in range(len(stack)):
        if stack[-1] == '*':
            stack.pop()
if flag and len(stack) == 0 and balanced>0:
    print('Yes',balanced)
else:
    print('No',balanced)


#(*)[**][][][]{}{}{}{{[[((***))]]}}