amount = list(map(int,input().split()))
for i in range(len(amount)):
   if i<2:
      print(1-amount[i], end=' ')
   elif i<5:
      print(2-amount[i], end=' ')
   else:
      print(8-amount[i])