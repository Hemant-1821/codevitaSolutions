def cal_m(m_req,Case,X_case):
    num = m_req+(Case*X_case)
    deno = 2*Case
    return num/deno

X1 = int(input())
X2 = int(input())
X3 = int(input())
Y = int(input())
#print(X1,X2,X3,Y)
X1_acc,X2_acc,X3_acc = None,None,None
#X1 Case
if (X2*2 + X3*3) < Y:
    m_req = Y - (X2*2 + X3*3)
    M = cal_m(m_req,1,X1)
    X1_acc = 100*M*1/X1
#X2 Case
if (X1 + X3*3) < Y:
    m_req = Y - (X1 + X3*3)
    M = cal_m(m_req,2,X2)
    X2_acc = 100*M*1/X2
    #print(m_req,M,X2_acc)

#X3 Case
if (X1 + X2*2) < Y:
    m_req = Y - (X1 + X2*2)
    M = cal_m(m_req,3,X3)
    X3_acc = 100*M*1/X3
    #print(m_req,M,X3_acc)

if X1_acc:
    if X1_acc.is_integer():
        X1_acc = int(X1_acc)
        print('Minimum Accuracy rate required for One mark question is {}%'.format(X1_acc))
    else:
        print('Minimum Accuracy rate required for One mark question is {:.2f}%'.format(X1_acc))
else:
    print('One mark question need not be attempted, so no minimum accuracy rate applicable')
if X2_acc:
    if X2_acc.is_integer():
        X2_acc = int(X2_acc)
        print('Minimum Accuracy rate required for Two mark question is {}%'.format(X2_acc))
    else:
        print('Minimum Accuracy rate required for Two mark question is {:.2f}%'.format(X2_acc))
else:
    print('Two mark question need not be attempted, so no minimum accuracy rate applicable')
if X3_acc:
    if X3_acc.is_integer():
        X3_acc = int(X3_acc)
        print('Minimum Accuracy rate required for Three mark question is {}%'.format(X3_acc))
    else:
        print('Minimum Accuracy rate required for Three mark question is {:.2f}%'.format(X3_acc))
else:
    print('Three mark question need not be attempted, so no minimum accuracy rate applicable')