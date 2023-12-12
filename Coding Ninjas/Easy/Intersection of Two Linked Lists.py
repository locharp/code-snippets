'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''
def findIntersection( firstHead, secondHead ):
    
    p = firstHead
    q = secondHead

    for i in range( 3 ):
        while p != None and q != None:
            if p == q:
                return p
            
            p = p.next
            q = q.next
        
        if p == None:
            p = secondHead
        elif q == None:
            q = firstHead
