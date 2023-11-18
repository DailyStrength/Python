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

example_dectionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

print("# 딕셔너리의 items() 함수")
print("items():", example_dectionary.items())
print()