def digitsSum(n):
    if n == 0:
        return 0
    
    return n % 10 + digitsSum(n//10)

ans = digitsSum(1234567)
print(ans)