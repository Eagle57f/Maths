def salaire1():
    v = 2000
    n = 0
    while v < 3000:
        n+=1
        v*=1.05
    return 2009 + n

print(salaire1()) # renvoie 2018


def salaire2():
    u = 2000
    n = 0
    v = 2000
    while u >= v:
        n+=1
        v*=1.05
        u+=115
    return 2009 + n

print(salaire2()) # renvoie 2016



def salaire3():
    u14 = 2000 + 115 * 14
    Su = 0.5 * 15 * (2000 + u14)
    Sv = 2000 * ((1 - 1.05**15) / (1-1.05))
    return f"Avec la proposition 1: {Su * 12}, avec la proposition 2: {round(Sv * 12)}"


print(salaire3()) # renvoie "Avec la proposition 1: 504900.0, avec la proposition 2: 517886"
