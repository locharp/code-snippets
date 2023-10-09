class Solution:
    
    def __init__( self ):
        self.ans = 0
        self.d = None
        self.p = { "0000" }        
        self.q = set()
        self.t = None
        
        
    def next( self, s ):
        for i in range( 4 ):
            if s[i] == "0":
                m = "9", "1"
            elif s[i] == "9":
                m = "8", "0"
            else:
                o = ord( s[i] )
                m = chr( o - 1 ), chr( o + 1 )
                
            for p in m:
                q = s[ : i ] + p + s[ i + 1 : ]
                
                if q not in self.d:
                    self.d.add( q )
                    self.q.add( q )
                    
        
        
    def openLock( self, deadends: List[str], target: str ) -> int:
        if "0000" in deadends:
            return -1
        
        self.d = set( deadends )
        self.t = target
        
        return self.open()
        
        
        
    def open( self ):
        if self.t in self.p:
            return self.ans
        elif len( self.p ) < 1:
            return -1
        
        for s in self.p:
            self.next( s )
                
        self.ans += 1
        self.p = self.q
        self.q = set()
        
        return self.open()
