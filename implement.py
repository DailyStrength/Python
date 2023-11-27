# for i in range(5):
#     for j in range(5):
#         print('(', i, ",", j, ')', end= " ")
#     print()

# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# x, y = 2, 2

# for i in range(4):
#     # 다음 위치
#     nx = x +dx[i]
#     ny = y + dy[i]
#     print(nx, ny)


# n = int(input())
# a = input()

# nx = 1
# ny = 1

# for i in range(1, n):
#     if a[i] == 'L':
#         ny -= 1
#     elif a[i] == 'R':
#         ny += 1
#     elif a[i] == 'U':
#         nx += 1
#     elif a[i] == 'D':
#         nx -= 1

# print(nx, ny)



n = int(input())
x, y = 1, 1
plans =input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)