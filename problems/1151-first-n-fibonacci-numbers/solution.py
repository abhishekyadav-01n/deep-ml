def first_n_fibonacci(n):
    a = 0
    b = 1
    if(n == 0):
        return []
    elif (n == 1):
        return [a]
    elif n == 2:
        return [a , b]

    result = [a,b]
    
    ans = 0
    x = 2
    while x != n:
        ans += (a+b)
        a = b
        b = ans
        x += 1
        result.append(ans)
        ans = 0
    
    return result
    pass