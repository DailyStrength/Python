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

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)    
