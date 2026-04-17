N = int(input())
for _ in range(N):
   R, S = map(str, input().split())
   P = str()
   for i in range(len(S)):
      for _ in range(int(R)):
         P=P+S[i]
   print(P)