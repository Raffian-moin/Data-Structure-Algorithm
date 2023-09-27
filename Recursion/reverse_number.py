def reverseNumber(number):
    if number == 0:
        return 0

    return 10 ** (len(str(number))-1) * (number%10) + reverseNumber(number//10)

ans = reverseNumber(12345)

print(ans)