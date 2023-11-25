# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)


# n, k = map(int, input().split())

# i = 0
# count = 0

# while n != 1:
#     if (n - i) % k == 0:
#         n = n/k
#         count += 1
#     else:
#         i += 1
#         n = n-i
#         count += 1

# print(count)


# n, k = map(int, input().split())

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (n//k)*k
#     result += (n-target)
#     n=target
#     # N이 K보다 적을 때 더이상 나눌 수 없을때 반복문 탈출
#     if n<k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n-1)
# print(result)

# n  = list(map(int, input("공백으로 구분된 자연수 다섯개 입력하세요: ").split()))

# count = 0
# result = 1
# while count < int(len(5)):
#     result *= n[count] 
#     count = count + 1
 
# print(result)
######################################################################
# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기 보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
    
# print(result)


