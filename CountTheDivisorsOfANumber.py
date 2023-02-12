def divisors(n):
    x = 1
    y = 1
    
    while y <= n / 2:
        if n % y == 0:
            x += 1
        y += 1    
    
    return x
