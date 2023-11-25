# revenue = 0
# day_revenue = 0
# day = 0

# with open('data/chicken.txt', 'r', encoding = 'UTF-8') as in_file:
#     for line in in_file:
#         data = line.strip().split(":")
#         revenue += int(data[1])
#         day += 1
#     print(revenue)
# day_revenue = revenue / day
# print("12월 매출 평균은 : ",day_revenue)  
# array = [i for i in range(20) if i % 2 == 1]

# print(array)

# array = []
# for i in range(20):
#     if i % 2 == 1:
#         array.append(i)

# print(array)    

# n = int(input())

# data = list(map(int,input().split()))
# data.sort(reverse = True)
# print(data)

# data = list(map(int,input().split()))
# data = list(map(int,input().split()))
# data = list(map((int,input().split())))
# data = list(map(int, input().split()))
# data = lits(map(int, iput().split()))
# data = list(map(int, input.split()))


# import sys
# data = sys.stdin.readline().rstrip()

# import sys
# data = sys.stdin.readline().restrip()

# import sys
# data = sys.stdin.readline().restrip()

# import
# print(data)


# scores = [90, 85, 77, 65, 97]
# cheating_student_list = [2, 4]

# for i in range(5):
#     if i + 1 in cheating_student_list:
#         continue
#     if scores[i] >= 80:
#         print(i +1, "번 학생은 합격입니다.")


for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()