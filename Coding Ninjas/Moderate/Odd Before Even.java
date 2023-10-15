public class Solution
{
	public static Node commonOddEven( Node head1, Node head2 )
	{
		Node odd = new Node( 0 );
		Node even = new Node ( 0 );
		Node o = odd;
		Node e = even;
		
		while ( head1 != null && head2 != null )
		{
			if ( head1.data == head2.data )
			{
				if ( head1.data % 2 == 0 )
				{
					e.next = head1;
					e = e.next;
				}
				else
				{
					o.next = head1;
					o = o.next;
				}

				head1 = head1.next;
				head2 = head2.next;
			}
			else if ( head1.data < head2.data )
			{
				head1 = head1.next;
			}
			else
			{
				head2 = head2.next;
			}
		}

		if ( even.next == null )
		{
			o.next = null;

			return odd.next;
		}
		else if ( odd.next == null )
		{
			e.next = null;

			return even.next;
		}
		else
		{
			e.next = null;
			o.next = even.next;

			return odd.next;
		}
	}
}
