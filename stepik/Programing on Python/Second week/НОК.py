bio = int(input())
inf = int(input())

m = max(bio, inf)
n = min(bio, inf)
nok = m

while nok % n != 0:
    nok += m

print(nok)