def minion_game( string ):
    
    kevin = stuart = 0
    n = len( string )
    
    for i in range( len( string ) ):
        if string[i] in "AEIOU":
            kevin += n - i
        else:
            stuart += n - i
            
    if kevin > stuart:
        print( "Kevin", kevin )
    elif stuart > kevin:
        print( "Stuart", stuart )
    else:
        print( "Draw" )
