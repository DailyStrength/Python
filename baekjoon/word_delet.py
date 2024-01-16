original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]
print(squared_list)

word = "hello"
uppercase_list = [char.upper() for char in word]
print(uppercase_list)

print("")

my_list = ['apple', 'banana', 'orange']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

word = "hello"
new_word = ''.join(char + str(index) for index, char in enumerate(word))
print(new_word)

print("")

