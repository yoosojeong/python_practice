import random
ch = int(input("임의의 좌표에 생성할 캐릭터 수를 입력해주세요:"))

def ch_location(ch):
    for i in range(0,ch):
        ch_x = random.randrange(0,ch)
        ch_y = random.randrange(0,ch)
        print("캐릭터 좌표(%d,%d)"%(ch_x,ch_y))
        location = [ch_x,ch_y]
        return (location)

while(1):
    for
        no = [ch_location(ch)

