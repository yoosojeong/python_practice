def sum_repeat(*args):
    sum_flus = 0
    for i in args:
        for j in i:
            sum_flus += int(j)

    return sum_flus

num = input("숫자를 입력해주세요:")
number = sum_repeat(num.split())
print(number)