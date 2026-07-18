message = input()
key = input()

# Please write your code here.
seen = set(['J'])
cipher = []
for char in key+'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    if char not in seen:
        seen.add(char)
        cipher.append(char)
cipher_board = [cipher[i:i+5] for i in range(0,25,5)]
cipher_coords = {char:(i//5,i%5) for i, char in enumerate(cipher)}
pairs = []
i = 0
while i<len(message):
    c1 = message[i]
    if i==len(message)-1:
        c2 = 'X'
        i+=1
    elif c1==message[i+1]:
        c2 = 'X' if c1!='X' else 'Q'
        i+=1
    else:
        c2 = message[i+1]
        i+=2
    pairs.append((c1,c2))
answer = ''
for c1,c2 in pairs:
    row1, col1 = cipher_coords[c1]
    row2, col2 = cipher_coords[c2]
    if row1==row2:
        c1 = cipher_board[row1][(col1+1)%5]
        c2 = cipher_board[row2][(col2+1)%5]
    elif col1==col2:
        c1 = cipher_board[(row1+1)%5][col1]
        c2 = cipher_board[(row2+1)%5][col2]
    else:
        c1 = cipher_board[row1][col2]
        c2 = cipher_board[row2][col1]
    answer+=c1+c2
print(answer)