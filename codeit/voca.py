with open("codeit/vocabulary.txt", "r", encoding="UTF-8") as file:
    for line in file:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        guess = input("{}: ".format(korean_word))
        
        
        #file_contents = file.readline()
        #word = file_contents.split()

 

# answer = input()

# if answer == word[1]:
#     print("맞았습니다!")
# else:
#     print("아쉽습니다. 정답은 {}입니다.".format(word[1]))
