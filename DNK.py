def get_total_time(heroes, n):
    res = 0
    if n == 1:
        res = sum(heroes)
    else:
        h = heroes[0:n]
        heroes = heroes[n:len(heroes)]
        while len(heroes) > 0:
            m = min(h)
            m_it = h.index(m)
            h[m_it] += heroes[0]
            del heroes[0]


        res = max(h)

    return res

print(get_total_time([11, 2, 3, 4], 2))