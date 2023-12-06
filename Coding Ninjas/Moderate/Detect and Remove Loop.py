from typing import *

def removeLoop( head :Node ) -> Node:

    c = d = head

    while c != None:
        if c.next is d:
            c.next = None
            break
        
        c = c.next

        if c.next is d:
            c.next = None
            break
        
        c = c.next
        d = d.next
    
    return head
