import random
param = input("N값의 좌표와 생성할 캐릭터 수를 입력하세요:")
params = param.split(",")

print(params)

num1 = int(params[0]) #태두리 크기
num2 = int(params[1]) #캐릭터 수

def pick_char(): #캐릭터의 좌표를 뽑는 함수
    x = random.randrange(0,num1) #캐릭터 x점
    y = random.randrange(0,num2)  #캐릭터 y점
    print("캐릭터 좌표 : (%d,%d)" %(x,y))

    return (x,y)



def not_overlap(num1,num2,location): #별과 캐릭터가 곂치지 않게 하는 함수
      for i in range(0,num1):
        for j in range(0,num1):
            if (j,i) == location:
                print("C",end = " ")
            else :
                print("*",end = " ")

        print("\n")

new = " "
while(1):
    for m in (0,num2-1):
        new += "pick_char()"
        for k in (0,num2-1):
            location = [(pick_char(),new)]

    for g in (0,num2-1):
        for f in (0,num2-1):
            for d in (0,num2-1):
                if location[f] == location[d]:
                    continue
                else:
                    break

not_overlap(num1,num2,location)