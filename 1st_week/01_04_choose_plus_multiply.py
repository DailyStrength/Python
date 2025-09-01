def find_max_plus_or_multiply(arr):
    result = arr[0]
    for x in arr[1:]:
        # 둘 중 하나라도 1 이하이면 더하기, 둘 다 2 이상이면 곱하기
        if result <= 1 or x <= 1:
            result += x
        else:
            result *= x
        
    return result

# 테스트
fn = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", fn([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", fn([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", fn([1,1,1,3,3,2,5]))
