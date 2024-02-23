public class Solution
{
    
    static Node reverseLinkedList
    ( Node head, Node tail )
    {
        if ( tail == null )
        {
            return head;
        }

        Node temp = tail.next;
        tail.next = head;
        
        return reverseLinkedList( tail, temp );
    }
    
    
    
    public static Node reverseLinkedList(Node head)
    {
        return reverseLinkedList( null, head );
    }
    
}
