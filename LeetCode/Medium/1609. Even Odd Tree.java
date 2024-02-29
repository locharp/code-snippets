class Solution
{

    public boolean isEvenOddTree
    ( TreeNode root )
    {
        ArrayDeque< TreeNode > deque = new ArrayDeque<>();
        deque.offer( root );
        int level = 0;
        int order = 1;

        while ( !deque.isEmpty() )
        {
            TreeNode node = deque.poll();
            int last = node.val;
            int n = deque.size();

            if ( last % 2 == level )
            {
                return false;
            }

            if ( node.left != null )
            {
                deque.offer( node.left );
            }

            if ( node.right != null )
            {
                deque.offer( node.right );
            }

            for ( int i = 0; i < n; i++ )
            {
                node = deque.poll();
                
                if ( node.val % 2 == level || ( node.val - last ) * order < 1 )
                {
                    return false;
                }

                last = node.val;

                if ( node.left != null )
                {
                    deque.offer( node.left );
                }

                if ( node.right != null )
                {
                    deque.offer( node.right );
                }
            }

            level = 1 - level;
            order *= -1;
        }

        return true;
    }

}
