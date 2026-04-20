from itertools import product
def solution(word):
    answer = 0
    vowels = list('AEIOU')
    dicts = []
    for i in range(1,6):
        for p in product(vowels, repeat=i):
            dicts.append(''.join(p))
    dicts.sort()
    answer = dicts.index(word)+1
    return answer