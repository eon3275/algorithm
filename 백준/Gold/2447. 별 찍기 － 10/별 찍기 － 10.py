def ans(n):
    if n==1:
        return ['*']
    stars = ans(n//3)
    line = []
    for s in stars:
        line.append(s*3)
    for s in stars:
        line.append(s+' '*(n//3)+s)
    for s in stars:
        line.append(s*3)
    return line

def do(n):
    line = ans(n)
    print('\n'.join(line))

do(int(input()))
    