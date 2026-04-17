A, B, C = map(int, input().split())
def ans(a,b,c):
    if b==0:
        return 1
    if b==1:
        return a%c
    temp = ans(a, b//2, c)
    if b%2==0:
        return (temp*temp)%c
    else:
        return (temp*temp*a)%c
print(ans(A,B,C))