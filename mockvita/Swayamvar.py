def swayamvar(bride,groom):
    groom = list(groom)
    for i in bride:
        if i in groom:
            groom.remove(i)
        else:
            break
    print(len(groom))
    
if __name__ == '__main__':
    leng = int(input())
    bride = input()
    groom = input()
    #print(li)
    swayamvar(bride, groom)
    
    