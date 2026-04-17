N = int(input())
db = []
for _ in range(N):
    age, name = input().split()
    db.append((int(age), name))
db.sort(key=lambda x: x[0])
for age, name in db:
    print(age, name)