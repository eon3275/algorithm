N, M = map(int,input().split(' '))
cards = list(map(int,input().split(' ')))
best = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            cards_sum = cards[i]+cards[j]+cards[k]
            if cards_sum >= best and cards_sum <= M:
                best = cards_sum
print(best)