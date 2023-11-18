# with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
#     for line in f:
#         print(line)

# Strip
# print("      abc   def     ".strip())

# split
# my_string = "1. 2. 3. 4. 5. 6"
# print(my_string.split(". "))

# full_name = "Kim, Yuna"
# print(full_name.split(", "))

# list_a = [1, 2, 3, 4, 5]
# list_reversed = reversed(list_a)

# print("# reversed() method")
# print("reversed([1, 2, 3, 4, 5]):", list_reversed)
# print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
# print()

# print("# reversed() 함수와 반복문")
# print("for i in reersed([1, 2, 3, 4, 5]):")
# for i in  reversed(list_a):
#     print("-",i)

# example_list = ["요소A", "요소B", "요소C"]

# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))

# example_dectionary = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C"
# }

# print("# 딕셔너리의 items() 함수")
# print("items():", example_dectionary.items())
# print()

# my_string = "1. 2. 3. 4. 5. 6"
# print(my_string.split("."))

# full_name = "Kim, Yuna"
# name_data = print(full_name.split(", "))

# print("     \n\n    3   \t  3   \n 5 7 11 \n\n".split())

# full_name = "Kim, Yuna"
# name_data = full_name.split(", ")
# last_name = name_data[0]
# first_name = name_data[1]

# # print(first_name, last_name)
# day = []

# with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
#     data = f.readlines()

# total_sales = 0
# days = 0

# for line in data:
#     day, sales = line.strip().split(":")
#     total_sales += int(sales)
#     days += 1

# average_sales = total_sales / days
# print("12월 코빠닭의 하루 평균 매출:", average_sales)

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

