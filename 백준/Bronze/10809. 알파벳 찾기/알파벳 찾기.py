Alphabet = [-1 for _ in range(26)]
S = input()
for i in range(ord('a'), ord('z')+1):
   for j in range(len(S)):
      if i==ord(S[j]):
         Alphabet[i-ord('a')]=j
         break
for i in range(len(Alphabet)):
   print(Alphabet[i], end=' ')