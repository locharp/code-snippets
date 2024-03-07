class Solution
{
    
    public ListNode middleNode
    ( ListNode head )
    {
        ListNode node = head.next;
        
        
        while ( node != null )
        {
            head = head.next;
            node = node.next;
            
            
            if ( node != null )
            {
                node = node.next;
            }
        }
        
        
        return head;
    }
    
}
