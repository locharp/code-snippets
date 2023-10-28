class Node:

    def __init__( self, data = 0, next = None ):

        self.data = data
        self.next = next



# Don't change the code above.
def f( n ):
    i, j = 1, 0

    while n is not None:
        j += n.data * i
        i *= 10
        n = n.next

    return j


        
def addTwoNumbers( head1: Node, head2: Node ) -> Node:
    
    m = f( head1 )
    n = f( head2 )
    n += m
    ans = Node( n % 10 )
    n //= 10
    c = ans

    while n > 0:
        c.next = Node( n % 10 )
        c = c.next
        n //= 10

    return ans
