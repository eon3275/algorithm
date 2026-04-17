def isbalanced(string):
    stack = []
    for c in list(string):
        if c=='(' or c=='[':
            stack.append(c)
        elif c==')' or c==']':
            if not stack: return False
            poped = stack.pop()
            if c==')' and poped!='(': return False
            elif c==']' and poped!='[': return False
    return not stack

string = input()
strings = []

while string!='.':
    strings.append(string)
    string = input()

for string in strings:
    print('yes' if isbalanced(string) else 'no')