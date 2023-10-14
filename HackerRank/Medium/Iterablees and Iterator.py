from itertools import permutations

input()
s = input()
k = int( input() )
p = count = 0

for i in permutations( s.split(), k ):
    p += 1

    if "a" in i:
        count += 1

print( count / p )
