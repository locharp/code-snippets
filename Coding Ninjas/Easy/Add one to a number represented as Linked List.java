/*************************************************************

Following is the class structure of the Node class:

    class Node {
		public int data;
		public Node next;

		Node(int data) {
			this.data = data;
			this.next = null;
	  	}
    }

*************************************************************/

public class Solution
{

	static int f
	( Node node )
	{
		if ( node == null )
		{
			return 1;
		}

		node.data += f( node.next );

		if ( node.data > 9 )
		{
			node.data = 0;
			return 1;
		}
		else
		{
			return 0;
		}
	}



	public static Node addOne
	( Node head )
	{
		int i = f( head );

		if ( i > 0 )
		{
			Node node = new Node( 1 );
			node.next = head;
			head = node;
		}

		return head;
	}

}
