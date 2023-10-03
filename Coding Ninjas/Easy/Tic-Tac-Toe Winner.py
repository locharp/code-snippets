def ticTacToeWinner( moves, n ):
    
    grid = [ [-10] * 3 for i in range( 3 ) ]
    r = [ -10 ] * 3
    s = [ -10 ] * 3
    t = u = 0
    
    for i in range( n ):
        grid[ moves[i][0] ][ moves[i][1] ] = i % 2
        
    for i in range( 3 ):
        r[i] = sum( grid[i] )
        s[i] = grid[0][i] + grid[1][i] + grid[2][i]
        t += grid[i][i]
        u += grid[i][ 2 - i ]
        
    if 0 in r or 0 in s or t == 0 or u == 0:
        return "player1"
    elif 3 in r or 3 in s or t == 3 or u == 3:
        return "player2"
    elif n < 9:
        return "uncertain"
    else:
        return "draw"
