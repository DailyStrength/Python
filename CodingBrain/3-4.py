x = 25
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while abs(ans**2 -x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1
print('추측횟수=', num_guesses)
if abs(ans**2-x) >= epsilon:
    print(x, '의 제곱근을 찾지 못했습니다.')
else:
    print(ans, '은(는)', x, '의 제곱근에 가깝습니다')