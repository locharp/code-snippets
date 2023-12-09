from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the Node class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addFirstAndReversedSecondHalf(head):
    
    if head == None:
        return None
        
    i = m = n = o = 0
    p = q = head
    
    while q != None:
        m = ( m * 10 ) + p.data
        p = p.next
        q = q.next

        if q != None:
            q = q.next

    while p != None:
        n += p.data * ( 10 ** i )
        i += 1
        p = p.next

    o = m + n
    ans = curr = Node( 0 )

    for i in str( o ):
        curr.next = Node( int( i ) )
        curr = curr.next

    return ans.next
