N = int(input())
room = 1
iter = 0
while(N>0):
    iter+=1
    N-=room
    room=6*iter
print(iter)