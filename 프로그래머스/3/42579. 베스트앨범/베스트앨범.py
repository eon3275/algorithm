def solution(genres, plays):
    answer = []
    tot_gen = {}
    songs = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        tot_gen[g] = tot_gen.get(g, 0)+p
        s = songs.get(g, [])
        s.append([p, i])
        songs[g] = s
    sorted_g = sorted(tot_gen.keys(), key=lambda x: -tot_gen[x])
    for g in sorted_g:
        curr = sorted(songs[g], key=lambda x:(-x[0], x[1]))
        for s in curr[:2]:
            answer.append(s[1])
    return answer