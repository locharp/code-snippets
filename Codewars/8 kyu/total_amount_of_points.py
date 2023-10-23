def points( games ):
    ans = 0
    
    for game in games:
        x, y = map( int, game.split( ":" ) )
        
        if x > y:
            ans += 3
        elif x == y:
            ans += 1
            
    return ans
