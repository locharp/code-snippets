public class Solution
{

    public static Node findMiddle
    ( Node head )
    {
        Node curr = head.next;

        while ( curr != null )
        {
            head = head.next;
            curr = curr.next;

            if ( curr != null )
            {
                curr = curr.next;
            }
        }

        return head;
    }

}
