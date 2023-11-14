def avoidTraps( obstacles, n ):
    
    for i in range( 2, max( obstacles ) + 2 ):
        t = True

        for j in obstacles:
            if j % i == 0:
                t = False
                break

        if t:
            return i

    return -1
