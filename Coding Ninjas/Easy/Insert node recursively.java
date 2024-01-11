public class Solution
{
    public static Node<Integer> insertNode
    ( Node<Integer> head, int pos, Node<Integer> newNode )
    {
        if ( pos < 1 )
        {
            newNode.next = head;
            return newNode;
        }

        Node<Integer> curr = head;

        while ( pos-- > 1 )
        {
            curr = curr.next;
        }

        newNode.next = curr.next;
        curr.next = newNode;

        return head;
    }
}
