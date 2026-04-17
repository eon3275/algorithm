N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split(' '))))
points.sort()
for i in range(N):
    print(points[i][0], points[i][1])