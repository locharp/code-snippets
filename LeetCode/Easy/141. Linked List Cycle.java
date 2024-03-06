public class Solution
{
    
    public boolean hasCycle
    ( ListNode head )
    {
        ListNode head2 = head;
        
        while ( head2 != null )
        {
            head = head.next;
            head2 = head2.next;
            
            if ( head2 == null )
            {
                return false;
            }
            else
            {
                head2 = head2.next;
            }
            
            if ( head == head2 )
            {
                return true;
            }
        }
        
        return false;
    }
    
}
