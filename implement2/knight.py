x = int(input())
y = int(input())
# 공백을 기준으로 두 수를 입력받음
# x가 가로 y가 세로를 의미

count = 8
#이동할 수 있는 경우의 수 

if x-1 < 1:
    count -= 1
elif x-2 < 1:
    count -= 1
elif y-1 < 1:
    count -= 1
elif y-2 < 1:
    count -= 1
elif x + 1 > 8:
    count -= 1
elif x + 2 > 8:
    count -= 1
elif y+1 > 8:
    count -= 1
elif y+2 > 8:
    count -= 1

print(count)



