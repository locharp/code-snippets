/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution
{
    
    public ListNode removeNthFromEnd
    ( ListNode head, int n )
    {
        ListNode curr = head;
        int m = 0;
        
        
        while ( curr != null )
        {
            curr = curr.next;
            m++;
        }
        
        
        if ( m == n )
        {
            return head.next;
        }
        
        
        n = m - n;
        curr = head;
        
        
        while ( n-- > 1 )
        {
            curr = curr.next;
        }
        
        
        curr.next = curr.next.next;
        
        
        return head;
    }
    
}
