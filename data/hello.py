# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a), output_a)
# print(type(output_b), output_b) 

# string_a = input("입력A> ")
# int_a = int(string_a)

# string_b = input("입력B> ")
# int_b = int(string_b)

# print("문자열 자료 :", string_a + string_b)
# print("숫자 자료 :", int_a + int_b)

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a), output_a)
# print(type(output_b), output_b)

# # 숫자를 입력받습니다.
# raw_input = input("inch 단위의 숫자를 입력해주세요: ")

# # 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
# inch = int(raw_input)
# cm = inch * 2.54  

# print(inch, "inch는 cm 단위로", cm, "cm입니다.")

# str_input = input("숫자입력> ")
# num_input = float(str_input)

# print()
# print(num_input, "inch")
# print((num_input * 2.54), "cm")

# str_input = input("원의 반지름 입력> ")
# num_input = float(str_input)
# print()
# print("반지름: ", num_input)
# print("둘레: ", 2 * 3.14 * num_input)
# print("넓이: ", 3.14 * num_input ** 2)

# a = input("문자열 입력> ")
# b = input("문자열 입력> ")

# print(a, b)

# temp = a
# a = b
# b = temp

# print(a, b)

# #format() 함수로 숫자를 문자열로 변환하기
# string_a = "{}".format(10)

# #출력하기
# print(string_a)
# print(type(string_a))

# # format() 함수로 숫자를 문자열로 변환하기
# format_a = "{}만원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)

# # 출력하기
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# # 정수
# output_a = "{:d}".format(52)

# # 특정 칸에 출력하기
# output_b = "{:5d}".format(52)

# a = input("> 1번째 숫자: ")
# b = input("> 2번째 숫자: ")
# print()

# print("{} + {} = {}".format(a, b, int(a) + int(b)))
# number = input("정수입력> ")
# number = int(number)

# if number > 0:
#     print("양수입니다")

# if number < 0:
#     print("음수입니다")

# if number == 0:
#     print("0입니다")

# import datetime

# now = datetime.datetime.now()

# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")

# import datetime
# now = datetime.datetime.now()

# if now.hour < 12:
#     print("현재 시각은 {}시로 오전입니다.".format(now.hour))

# if now.hour >= 12:
#     print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# number = input("정수입력> ")

# last_character = number[-1]

# last_number = int(last_character)

# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다")

# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수입니다")

# number = input("정수입력> ")
# number = int(number)

# if number % 2 == 0:
#     print("짝수입니다")

# if number % 2 == 1:
#     print("홀수입니다")

# number = input("정수입력> ")
# last_character = number[-1]

# if last_character in "02468":
#     print("짝수입니다")

# if last_character in "13579":
#     print("홀수입니다")

# a = float(input("> 1번째 숫자: "))
# b = float(input("> 2번째 숫자: "))
# print()

# if a > b:
#     print("처음입력했던 {}가 {}보다 더 큽니다".format(a, b))

# if a < b:
#     print("두번째로 입력했던 {}가 {}보다 더 큽니다.".format(b, a))


# list_a = [1, 2, 3]
# list_b = [4, 5, 6]

# print("# 리스트")
# print("list_a = ", list_a)
# print("list_b = ", list_b)
# print()

# print("# 리스트 기본 연산자")
# print("list_a + list_b = ", list_a + list_b)
# print("list_a * 3 = ", list_a * 3)
# print()

# print("# 길이 구하기")
# print("len(list_a) = ", len(list_a))

# list_a = [1, 2, 3]

# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)


# list_a = [0, 1, 2, 3, 4, 5]
# print("# 리스트의 요소 하나 제거하기")

# del list_a[1]
# print("del list_a[1]:", list_a)

# list_a.pop(2)
# print("pop(2): ", list_a)

# list_c = [1, 2, 1, 2]
# list_c.remove(2)
# print(list_c)

# list_a = [273, 32, 103, 57, 52]
# print(273 not in list_a)

# for i in range(100):
#     print("출력")

# array = [273, 32, 103, 57, 52]

# for element in array:
#     print(element)

# list_of_list = [
#     [1, 2, 3], 
#     [4, 5, 6, 7], 
#     [8, 9]
# ]

# # for items in list_of_list:
# #     print(items)

# for items in list_of_list:
#     for item in items:
#         print(items)

# array = [273, 32, 103, 57, 52]

# for elemet in array:
#     print(elemet)

# list_of_list = [
#     [1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9]
# ]

# for items in list_of_list:
#     for item in items:
#         print(items)

# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# print("name: ", dictionary["name"])
# print("type: ", dictionary["type"])
# print("ingredient: ", dictionary["ingredient"])
# print("origin: ", dictionary["origin"])
# print()

# dictionary["name"] = "8D 건조 망고"
# print("name:", dictionary["name"])


# dictionary = {}

# print("요소 추가 이전:", dictionary)

# dictionary["name"] = "새로운이름"
# dictionary["head"] = "새로운 정신"
# dictionary["body"] = "새로운 몸"

# print("요소 추가 이후:", dictionary)
 
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임"
#     "ingredient": ["망고", "설탕", ""]
# } 

# for i in range(5):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(5, 10):
#     print(str(i) + "=반복 변수")
# print()

# for i in range(0, 10, 3):
#     print(str(i) + "= 반복변수")
# print()


# array = [273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print("{}번째 반복: {}".format(i, array[i]))


# for i in range(4, 0-1, -1):
#     print("현재 반복 변수: {}".format(i))

# output=""

# for i in range(1, 10):
#     for j in range(0, i):
#         output += "*"
#     output += "\n"

# print(output)

# output =""

# for i in range(1, 15):
#     for j in range(14, i, -1):
#         output += ' '
#     for k in range(0, 2*i-1):
#         output += '*'
#     output += '\n'

# print(output)


# i = 0
# while i <10:
#     print("{}번째 반복입니다.".format(i))
#     i+=1

# list_test = [1, 2, 1, 2]
# value = 2

# while value in list_test:
#     list_test.remove(value)

# print(list_test)

# import time
# number = 0
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number +=1

# print("5초 동안 {}번 반복했습니다.".format(number))

# i = 0

# while True:
#     print("{}번째 반복문입니다.".format(i))
#     i = i+1
#     input_text = input(">종료하시겠습니까?(y/n): ")
#     if input_text in["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# example_list = ["요소A", "요소B", "요소C"]

# print("#단순출력")

# import datetime
# pi_day = datetime.datetime(2020, 3, 14)
# print(pi_day)
# # print(type(pi_day))
# import datetime

# today = datetime.datetime.now()
# pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
# print(today - pi_day)
# print(type(today-pi_day))

# name = input("이름을 입력하세요: ")
# print(name)

# import random
# random_num = random.randrange(1,20)
# count = 4
# while count > 0:
#     input_num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:".format(count)))
#     if random_num > input_num:
#         print("Up")
#     elif random_num < input_num:
#         print("Down")
#     else:
#         print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(5-count))
#         break
#     count -= 1
#     if count == 0:
#         print("아쉽습니다. 정답은 {}였습니다.".format(random_num))


    