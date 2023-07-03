/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution
{

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function middleNode( $head )
    {
        $count = 0;
        $curr = $head;
        
        while ($curr->next != null)
        {
            $curr = $curr->next;
            $count++;
        }
        
        $count /= 2;
        
        while ($count > 0)
        {
            $head = $head->next;
            $count--;
        }
        
        return $head;
    }
}