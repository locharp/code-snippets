public class Solution
{
    
    static Node insert
    ( int k, int val, Node head )
    {
        Node node = new Node( val );

        if ( k < 1 )
        {
            node.next = head;
            return node;
        }

        Node curr = head;

        while ( k-- > 1 )
        {
            curr = curr.next;
        }

        node.next = curr.next;
        curr.next = node;
        node.prev = curr;

        if ( node.next != null )
        {
            node.next.prev = node;
        }

        return head;
    }

}
