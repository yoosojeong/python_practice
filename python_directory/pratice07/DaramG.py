import random
ground1 = input("화면의 크기와 플레이어의 좌표(x,y)를 입력해주세요:")
ground = ground1.split(",")
background = int(ground[0])

def daramG_location():
    num = 0
    daramG_x = random.randrange(0,background)
    daramG_y = random.randrange(0,background)
    print("다람쥐 좌표 (%d,%d)"%(daramG_x,daramG_y))
    return (daramG_x,daramG_y)

player_x = int(ground[1])
player_y = int(ground[2])
print("플레이어 좌표(%d,%d)"%(player_x,player_y))
player = [player_x,player_y]

def star_location(background,double,player):
    if(5 <= background and  background <= 20):
        for i in range(0,background):
            for j in range(0,background):
                if (j,i) == double[0]:
                    print("D",end=" ")
                elif (j,i) == double[1]:
                    print("D",end=" ")
                elif j == player_x and i == player_y:
                    print("C",end=" ")
                else:
                    print("*",end=" ")
            print("\n")

while(1):
    double = [daramG_location(),daramG_location()]
    if double[0] == player or double[1] == player:
        continue
    else:
        break

star_location(background,double,player)