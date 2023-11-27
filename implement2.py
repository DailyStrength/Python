n = int(input("0부터 23까지의 정수를 입력하시오"))

count = 0

if n < 3: # 시간이 3시 이전일때
    for i in range(0, n+1):
        for j in range(0, 60):
            if ((j-3) % 10 == 0) or (0<= (j - 30) <=9):
                count += 60
            else:
                count += 15
elif n ==3: # 시간이 3시일때
    for i in range(0, 3):
        for j in range(0, 60):
            if ((j-3) % 10 == 0) or (0<= (j-30) <= 9):#3이 들어간 분
                count += 60
            else: #3이 들어가지 않은 분
                count += 15
        count += 3600
elif n > 3: # 시간이 3시 이후일때
    for i in range(0, 3):
        for j in range(0, 60):
            if ((j-3) % 10 == 0) or (0<= (j-30) <= 9): 
                count += 60
            else:
                count += 15
        count += 3600
    for i in range(4, n+1):
        for j in range(0, 60):
            if ((j-3) % 10 == 0) or (0<= (j - 30) <=9):
                count += 60
            else:
                count += 15
print(count)

# 예외 처리 필요 // 중복된 count가 들어간것으로 예상됨
# 예를 들어 33분일때 33초일때 제외해야함