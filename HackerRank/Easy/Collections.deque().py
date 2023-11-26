from collections import deque

d = deque()

for i in range( int( input() ) ):
    inp = input().split()
    
    if inp[0] == "append":
        d.append( inp[1] )
    elif inp[0] == "appendleft":
        d.appendleft( inp[1] )
    elif inp[0] == "pop":
        d.pop()
    else:
        d.popleft()
        
print( " ".join( d ) )
