class Solution:
    def isValid( self, s: str ) -> bool:
        q = deque()
        
        for p in s:
            if p == ")":
                if len( q ) == 0 or q.pop() != "(":
                    return False
            elif p == "]":
                if len( q ) == 0 or q.pop() != "[":
                    return False
            elif p == "}":
                if len( q ) == 0 or q.pop() != "{":
                    return False
            else:
                q.append( p )
                
        return len( q ) == 0