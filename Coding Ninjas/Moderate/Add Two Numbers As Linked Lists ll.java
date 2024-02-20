import java.util.* ;
import java.io.*; 
/************************************************************

    Following is the linked list node structure:
    
    class ListNode<T> {
 
		public T data;
		public ListNode<T> next;

		public ListNode(T data) {
			this.data = data;
		}
	}

************************************************************/

public class Solution
{

	static ListNode< Integer > reverseList
	( ListNode head, ListNode tail )
	{
		if ( tail == null )
		{
			return head;
		}

		ListNode< Integer > temp = tail.next;
		tail.next = head;
		
		return reverseList( tail, temp );
	}



	public static ListNode< Integer > addTwoLists
	( ListNode< Integer > first, ListNode< Integer > second )
	{
		first = reverseList( null, first );
		second = reverseList( null, second );
		Integer o = 0;
		ListNode< Integer > head = new ListNode<>( 0 );
		ListNode< Integer > curr = head;

		do
		{
			if ( first != null )
			{
				o += first.data;
				first = first.next;
			}
			
			if ( second != null )
			{
				o += second.data;
				second = second.next;
			}

			curr.next = new ListNode<>( o % 10 );
			curr = curr.next;
			o /= 10;
		}
		while ( first != null || second != null );

		if ( o > 0 )
		{
			curr.next = new ListNode<>( o );
		}

		head = reverseList( null, head.next );
		
		return head;
	}

}
