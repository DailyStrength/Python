memo = {}
def f(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        temp = f(n-1) + f(n-2)
        memo[n] = temp
        return temp

print(f(10))
print(memo)