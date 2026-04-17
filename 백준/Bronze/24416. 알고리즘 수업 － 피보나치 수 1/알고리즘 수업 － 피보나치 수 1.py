def fibonacci(n):
    global code2
    f = [1]
    f.extend([1, 1])
    for i in range(3, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
    
n = int(input())
print(fibonacci(n), n-2)