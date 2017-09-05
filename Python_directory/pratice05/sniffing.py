def sniffing(*num):
    sum = 0
    for i in num :
        for j in i:
            j_1 = int(j)
            if j_1  % 2 == 0 :
                sum += j_1

            else :
                sum -= j_1
    return sum

number_first = input("숫자를 여러 개 입력해주세요:")
number_second = sniffing(number_first.split())
print(number_second)
