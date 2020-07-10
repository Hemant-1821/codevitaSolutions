for _ in range(int(input())):
    string = input().strip()
    #print(string)
    stack = []
    flag = True
    main,user = False,True
    count = 0
    if string[0] == '{':
        #print(string[0])
        stack.append('{')
        stack.append('S')
    else:
        flag = False
    for i in range(1,len(string)):
        #print(i)
        #print(string[1])
        if string[i] == ' ':
            continue
        if string[i] == '<' and stack[-1] != '(' and stack[-1] != '{' and flag and main == False:
            #print('<')
            stack.append('<')
            main = True
        elif string[i] == '>' and stack[-1]=='<':
            #print('>')
            stack.pop()
        elif string[i] == '(' and stack[-1] != '(' and stack[-1] != '{'and stack[-1] != '<' and flag:
            #print('(')
            stack.append('(')
            user = True
            count = 0
        elif string[i] == ')' and stack[-1] == '(' and count <= 100:
            #print(')')
            stack.pop()
            user = False
        elif string[i] == '{' and stack[-1] != 'S' and len(stack) > 0:
            #print('{')
            stack.append('{')
        elif string[i] == '}' and (stack[-1] == '{' or stack[-1] == 'S'):
            if stack[-1] == 'S':
                #print('S','}')
                stack.pop()
                stack.pop()
            else:
                #print('}')
                stack.pop()
        elif string[i] == 'P':
            if user:
                count += 1
            #print('P',count)
        else:
            flag = False
            break
    #print(flag,len(stack),main)
    if flag and len(stack) == 0 and main:
        print('No Compilation Errors')
    else:
        print('Compilation Errors')