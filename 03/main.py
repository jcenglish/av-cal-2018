import re
from collections import Counter


def getClaims():
    with open('input.txt', 'r') as file:
        claims = {tuple(int(d) for d in re.findall('(\d+)', line))
                  for line in list(file)}
        file.close

    return claims


def plotClaims(claims=getClaims()):
    fabric = {}
    for claim in claims:

        id = claim[0]
        left = claim[1]
        top = claim[2]
        w = claim[3]
        h = claim[4]

        for i in range(h):
            for j in range(w):
                coord = '%d,%d' % (i+top, j+left)
                if coord not in fabric:
                    fabric[coord] = [claim]
                else:
                    fabric[coord].append(claim)

    return fabric


def countOverlaps(fabric=plotClaims()):
    return sum(1 for square in fabric.values() if len(square) > 1)


def getNonOverlappingClaims(fabric=plotClaims()):
    c = Counter(claim[0] for claim in fabric.values() if len(claim) == 1)

    return [k[0][0] for k in c.items() if k[0][3]*k[0][4] == k[1]][0]
