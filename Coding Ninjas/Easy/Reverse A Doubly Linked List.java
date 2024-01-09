public class Solution
{
    public static Node reverseDLL( Node head )
    {
        Node curr = head.next;
        Node temp = null;
        head.next = null;

        while ( curr != null )
        {
            if ( curr.next != null )
            {
                temp = curr.next;
            }
            else
            {
                temp = null;
            }

            curr.next = head;
            head = curr;
            curr = temp;
        }

        return head;
    }
}
