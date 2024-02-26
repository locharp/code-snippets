public class Solution
{

    public static boolean detectCycle
    ( Node head )
    {
        Node curr = head;

        while ( curr != null )
        {
            head = head.next;
            curr = curr.next;

            if ( curr == null )
            {
                return false;
            }

            curr = curr.next;

            if ( curr == head )
            {
                return true;
            }
        }

        return false;
    }

}
