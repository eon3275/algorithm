def temp(num): # 이 숫자가 종말의 수인지 판별하는 함수
    counter = 0
    while num!=0 and counter!=3:
        if num%10 == 6: # if digit is 6
            counter += 1
            num = num // 10
        else:
            counter = 0 # start all over
            num = num // 10
    if counter == 3 : return True
    else : return False
        
N = int(input())
cnt = 0
num = 0
while cnt != N: # N번째 숫자일때 탈출
    num += 1
    if temp(num): cnt += 1
print(num)