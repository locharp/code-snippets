import re

S = input()
k = input()
pattern = re.compile( k )
match = pattern.search( S )

if match is None:
    print( ( -1, -1 ) )
else:
    while match is not None:
        i = match.start()
        j = match.end() - 1
        
        print( ( i, j ) )
        
        match = pattern.search( S, i + 1 )
