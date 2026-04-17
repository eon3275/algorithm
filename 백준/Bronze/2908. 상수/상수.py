A, B = input().split()
for i in range(3):
   if int(A[2-i]) > int(B[2-i]):
      print(int(A[::-1]))
      break
   elif int(A[2-i]) < int(B[2-i]):
      print(int(B[::-1]))
      break
   else:
      continue