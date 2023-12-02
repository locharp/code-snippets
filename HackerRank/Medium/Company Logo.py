from collections import Counter

if __name__ == "__main__":
    s = input()
    c = Counter( s )
    ans = sorted( c, key = lambda x: ( -c[x], x ) )[ : 3 ]
    
    for i in ans:
        print( i, c[i] )
