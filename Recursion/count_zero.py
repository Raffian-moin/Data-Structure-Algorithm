def countZero(number, count):
    if number == 0:
        return count
    
    if number % 10 == 0:
        count += 1

    return countZero(number//10, count)

ans = countZero(10000, 0)
print(ans)