from typing import List

def collidingAsteroids( asteroids: List[int] ) -> List[int]:
    
    ans = []

    for i in asteroids:
        if i > 0:
            ans.append( i )
        else:
            while len( ans ) > 0 and ans[-1] > 0 and ans[-1] < -i:
                ans.pop()

            if len( ans ) < 1 or ans[-1] <= 0:
                ans.append( i )
            elif ans[-1] == -i:
                ans.pop()
                
    return ans
