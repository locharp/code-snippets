# Following is the List Node Class Structure:
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

        

def rearrangeList( head ):

    if head is None:
        return head

    a = []
    curr = head.next

    while curr is not None:
        a.append( curr )
        curr = curr.next

    curr = head

    while len( a ) > 0:
        curr.next = a.pop()
        curr = curr.next

        if len( a ) > 0:
            curr.next = a.pop( 0 )
            curr = curr.next

    curr.next = None

    return head
