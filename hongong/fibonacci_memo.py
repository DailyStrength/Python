# 메모 변수를 만듭니다.
dictionary = {
    1:1,
    2:1
}

# 원하는 수를 입력받습니다.
n = input("원하는 ")



# 함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어있으면 메모된 값을 리턴
        print("{}의 피보나치 수는:{}".format(n, dictionary[n]))
        return 0
    else:
        output = fibonacci[n-1] + fibonacci[n-2]
        dictionary[n] = output
        return output
    
print("{}의 피보나치 수는:{}".format(n, dictionary[n]))

    


