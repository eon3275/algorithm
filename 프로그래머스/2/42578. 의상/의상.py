def solution(clothes):
    answer = 1
    wardrobe = {}
    for cloth in clothes:
        category = cloth[1]
        wardrobe[category] = wardrobe.get(category, 0)+1
    for category in wardrobe.values():
        answer *= category+1 
    answer-=1 # wear nothing.
    return answer