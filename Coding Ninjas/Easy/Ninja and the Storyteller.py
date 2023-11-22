def countStories( x, y, z, w = 0 ):
    
    w += z // y
    
    if w < x:
        return w
    
    return w // x * x + countStories( x, y, y * w // x, w % x )
