#2보다 큰 정수가 소수인지 테스트 합니다. 소수가 아니면 가장 작은 제수를 출력합니다.
x = int(input('2보다 큰 정수를 입력하세요'))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
if smallest_divisor == None:
    print(x, '의 가장 작은 제수는', smallest_divisor,'입니다.')
else:
    print(x, '은(는) 소수입니다.')