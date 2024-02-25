public class Solution
{

    static Node copyAndReverse
    ( Node head, Node tail, Node copy )
    {
        if ( tail == null )
        {
            return head;
        }

        Node copyTail = new Node( tail.data );
        copy.next = copyTail;
        Node temp = tail.next;
        tail.next = head;

        return copyAndReverse( tail, temp, copyTail );
    }



    static boolean equal( Node m, Node n )
    {
        if ( m == null )
        {
            if ( n == null )
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if ( n == null )
        {
            return false;
        }
        else if ( m.data == n.data )
        {
            return equal( m.next, n.next );
        }
        else
        {
            return false;
        }
    }


     
    public static boolean isPalindrome
    ( Node head )
    {
        Node copyHead = new Node( 0 );
        head = copyAndReverse( null, head, copyHead );
        
        return equal( head, copyHead.next );
    }
    
}
