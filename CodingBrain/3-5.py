x = 25
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 -x) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans=', ans)
    num_guesses += 1
    if ans**2 < x:
         low = ans
    else:
         high = ans
    ans = (high + low)/2
print('추측횟수 = ', num_guesses)
print(ans, '는', x,'의 제곱근에 가깝습니다.')