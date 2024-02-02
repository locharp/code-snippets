public class Solution
{

    public static Node constructLL
    ( int[] arr )
    {
        Node head = new Node( arr[0] );
        Node curr = head;

        for ( int i = 1; i < arr.length; i++ )
        {
            curr.next = new Node( arr[i] );
            curr = curr.next;
        }

        return head;
    }

}
