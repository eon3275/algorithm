def preorder(node, bt):
    print(node[0], end='')
    if node[1]!='.':
        for i in bt:
            if i[0] == node[1]:
                preorder(i, bt)
    if node[2]!='.':
        for i in bt:
            if i[0] == node[2]:
                preorder(i, bt)

def inorder(node, bt):
    
    if node[1]!='.':
        for i in bt:
            if i[0] == node[1]:
                inorder(i, bt)
    print(node[0], end='')
    if node[2]!='.':
        for i in bt:
            if i[0] == node[2]:
                inorder(i, bt)

def postorder(node, bt):
    if node[1]!='.':
        for i in bt:
            if i[0] == node[1]:
                postorder(i, bt)
    if node[2]!='.':
        for i in bt:
            if i[0] == node[2]:
                postorder(i, bt)
    print(node[0], end='')
            



n=int(input())
bt=[]
for i in range(n):
    bt.append(list(input().split()))

preorder(bt[0], bt)
print()
inorder(bt[0], bt)
print()
postorder(bt[0], bt)
