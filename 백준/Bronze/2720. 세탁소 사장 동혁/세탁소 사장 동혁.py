n = int(input())
List = []
for _ in range(n):
    charge = int(input())
    Q = charge // 25
    charge %= 25
    D = charge // 10
    charge %= 10
    N = charge // 5
    charge %= 5
    P = charge
    List.append([Q, D, N, P])
for i in range(n):
    for j in range(4):
        print(List[i][j], end=' ')
    print()