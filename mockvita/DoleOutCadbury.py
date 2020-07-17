from sys import stdin, stdout  

def cad(l,b,count):
    while 1:
        if l%b == 0:
            count += l//b
            break
        else:
            temp = l%b
            count += l//b
            l = b
            b = temp
    return count

if __name__ == '__main__':
    P = int(stdin.readline())
    Q = int(stdin.readline())
    R = int(stdin.readline())
    S = int(stdin.readline())
    stud = 0
    for i in range(P,Q+1):
        for j in range(R,S+1):
            stud += cad(i, j, 0)
    stdout.write(str(stud))