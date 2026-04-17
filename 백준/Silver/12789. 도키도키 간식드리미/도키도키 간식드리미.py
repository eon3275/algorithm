N = int(input())
stack0 = list(map(int, input().split()))[::-1]
stack1 = []
cnt = 1
while stack0:
    if stack0[-1]==cnt:
        stack0.pop()
        cnt+=1
    elif stack1 and stack1[-1]==cnt:
        stack1.pop()
        cnt+=1
    else:
        stack1.append(stack0.pop())
while stack1:
    if stack1[-1]==cnt:
        stack1.pop()
        cnt+=1
    else: break
print('Nice' if cnt==N+1 else 'Sad')