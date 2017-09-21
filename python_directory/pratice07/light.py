#동:E 서:W 남:S 북:N
len = input("크기를 입력해주세요:")
leng = [len,len]
len_1 = int(leng[0])
len_2 = int(leng[1])

stick_r1 = [0,1]
stick_r2 = [0,2]
stick_l1 = [2,1]
stick_l2 = [2,3]
light = [2,2]

if 1<= len_1 and len_1<=30 :
    for i in range(0,len_1):
        for j in range(0,len_2):
            if j == stick_r1[0] and i == stick_r1[1]:
                print("/",end=" ")
            elif j == stick_r2[0] and i == stick_r2[1]:
                print("/",end=" ")
            elif j == stick_l1[0] and i == stick_l1[1]:
                print("\\",end=" ")
            elif j == stick_l2[0] and i == stick_l2[1]:
                print("\\",end=" ")
            elif j == light[0] and i == light[1]:
                print("O",end=" ")
            else:
                print(".",end=" ")
        print("\n")


def dot(direction,point):
    newx = point[0]
    newy = point[1]
    if direction == "W" :
        newx -= 1
    elif direction == "E":
        newx += 1
    elif direction == "S":
        newy += 1
    elif direction == "N":
        newy -= 1
    else :
     pass
    
     return (direction,newx,newy)
nextP = dot('W', (10, 5))
print(nextP)

# nextP : W (9, 5)
#L2:S(2,2) R2:W(2,2) D0:E(2,2) R3:N(2,2)
def result(direction,newx,newy):
    if newx == 2 and newy == 2:
        if direction == "S":
            print("L 2")
        elif direction == "W":
            print("R 2")
        elif direction == "E":
            print("D 0")
        elif direction == "N":
            print("R 3")

result(direction,newx,newy)