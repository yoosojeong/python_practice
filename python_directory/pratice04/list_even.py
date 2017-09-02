#입력받은 수 중 짝수만 을 더해 출력
def list(*even_first):
    sum = 0
    for i in even_first:
        for j in i:
            l = int(j)
            if l%2 == 0:
                sum += l
    return sum

num = input("숫자를 입력해주세요:")
result = list(num.split())
print(result)