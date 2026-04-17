import sys
N = int(sys.stdin.readline().rstrip())
db = set()
for _ in range(N):
    name, status = sys.stdin.readline().rstrip().split()
    if status == 'enter':
        db.add(name)
    else:
        db.remove(name)
db = sorted(db, reverse=True)
for name in db:
    sys.stdout.write(name+'\n')