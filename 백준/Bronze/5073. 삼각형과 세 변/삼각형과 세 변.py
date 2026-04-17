nums=[]
while True:
    a,b,c = map(int, input().split())
    if a+b+c==0:
        break
    nums.append([a,b,c])

for num in nums:
    a,b,c = num[0], num[1], num[2]
    m = max(num)
    if m>=sum(num)-m:
        print("Invalid")
    elif a==b and b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")
