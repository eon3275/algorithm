string = input()
S = 0
for i in range(len(string)):
   temp = ord(string[i])
   if ord('A') <= temp and temp <= ord('C'):
      S+=3
   elif ord('D') <= temp and temp <= ord('F'):
      S+=4
   elif ord('G') <= temp and temp <= ord('I'):
      S+=5
   elif ord('J') <= temp and temp <= ord('L'):
      S+=6
   elif ord('M') <= temp and temp <= ord('O'):
      S+=7
   elif ord('P') <= temp and temp <= ord('S'):
      S+=8
   elif ord('T') <= temp and temp <= ord('V'):
      S+=9
   elif ord('W') <= temp and temp <= ord('Z'):
      S+=10
print(S)