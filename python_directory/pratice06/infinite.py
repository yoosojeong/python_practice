#함수 변수 복수개 입력받는 방법
#순서가 바껴서 나옴
def infinite(*num):
    list_blank = " "
    list = str(list_blank)
    for i in num:
        for j in i:
            list = j + list
    return list

list = input("숫자를 입력해주세요:")
num = infinite(list.split())
print(num)