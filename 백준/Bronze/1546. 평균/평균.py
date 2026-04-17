N = int(input())
arr = list(map(int,input().split()))
s = 0
m = max(arr)
for i in range(N):
   arr[i] = arr[i]/m*100
   s+=arr[i]
print(s/N)