def binaryToInteger( n: int, head ) -> int:
    
    ans = 0
    
    while head != None:
        ans = ( ans * 2 ) + head.data
        head = head.next
        
    return ans
