class Solution:
    def asteroidCollision( self, asteroids: List[int] ) -> List[int]:
        st = []
        
        for a in asteroids:
            if a > 0:
                st.append( a )
            elif len( st ) > 0:
                while len( st ) > 0:
                    z = st.pop()
                    if z > 0:
                        if z > -a:
                            st.append( z )
                            break
                        elif z == -a:
                            break
                    else:
                        st += [ z, a ]
                        break
                else:
                    st.append( a )
            else:
                st.append( a )
                    
        return st