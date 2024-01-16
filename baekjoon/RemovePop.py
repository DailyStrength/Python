my_list = [1, 2, 3, 4, 5]
element_to_remove = 3

if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"{element_to_remove}가 제거된 후 리스트: {my_list}")
else:
    print(f"{element_to_remove}를 찾을 수 없습니다.")

my_list2 = [1, 2, 3, 4, 5]
index_to_remove = 2

if index_to_remove < len(my_list):
    removed_element = my_list.pop(index_to_remove)
    print(f"인덱스 {index_to_remove}에 있는 {removed_element}가 제거된 후 리스트: {my_list}")
else:
    print(f"인덱스 {index_to_remove}는 리스트의 범위를 벗어납니다.")