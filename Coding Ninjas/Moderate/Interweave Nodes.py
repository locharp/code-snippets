'''
    Following is the class structure of the Node class:

    class Node:
        def __init__(self, data):

            self.data = data
            self.next = None
                
'''

def interweaveNodes( head1, head2 ):
    
    p = q = None
    
    if head1 != None:
        p = head1
    elif head2 != None:
        p = head2.next
    
    if head2 != None:
        q = head2
    elif head1 != None:
        q = head1.next

    ans = [ p, q ]
    
    if head1 != None:
        head1 = head1.next

    if head2 != None:
        head2 = head2.next
    
    while head1 != None or head2 != None:
        
        if head1 != None:
            q.next = head1
            q = q.next
            head1 = head1.next
            
        if head2 != None:
            p.next = head2
            p = p.next
            head2 = head2.next
            
        if head1 != None:
            p.next = head1
            p = p.next
            head1 = head1.next
            
        if head2 != None:
            q.next = head2
            q = q.next
            head2 = head2.next
    
    if p != None:
        p.next = None
    
    if q != None:
        q.next = None
    
    return ans
