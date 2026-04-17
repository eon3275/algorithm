def solution(nums):
    pokemons = {}
    for p in nums:
        pokemons[p] = pokemons.get(p, 0) + 1
    answer = min(len(nums)//2, len(pokemons))
    return answer