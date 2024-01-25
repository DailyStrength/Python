# 2보다 큰 정수가 소수인지 테스트 소수가 아니면 가장 작은 제수를 출력
x = int(input('2보다 큰 정수를 입력하세요: '))
smallest_divisor = None
if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x%guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print(x, '의 가장 작은 제수는', smallest_divisor, '입니다')
else:
    print(x, '은(는) 소수입니다.')