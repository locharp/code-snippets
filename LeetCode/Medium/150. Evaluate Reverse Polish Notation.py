class Solution:
    
    def evalRPN( self, tokens: List[str] ) -> int:
        
        nums = []
        
        for t in tokens:
            if t[-1].isdecimal():
                nums.append( int( t ) )
            else:
                o = nums.pop()
                
                if t == "*":
                    nums[-1] *= o
                elif t == "/":
                    nums[-1] = int( nums[-1] / o )
                elif t == "+":
                    nums[-1] += o
                else:
                    nums[-1] -= o
            
        return nums[0]
