def stepCount(number, count):
    if number == 0:
        return count
    
    count += 1
    
    if number & 1:
        number -= 1
    else:
        number //= 2
    
    return stepCount(number, count)

ans = stepCount(9, 0)
print(ans)