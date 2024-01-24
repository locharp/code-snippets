class Solution
{
  
    int[] arr;
    int ans;



    Solution()
    {
        this.arr = new int[10];
        this.ans = 0;
    }



    int f()
    {
        int c = 0;

        for ( int i : this.arr )
        {
            c += i % 2;
        }

        if ( c < 2 )
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    
    
    
    public int pseudoPalindromicPaths( TreeNode root )
    {
        if ( root == null )
        {
            return this.ans;
        }

        this.arr[root.val]++;

        if ( root.left == null )
        {
            if ( root.right == null )
            {
                this.ans += this.f();
            }
            else
            {
                this.pseudoPalindromicPaths( root.right );
            }
        }
        else
        {
            if ( root.right != null )
            {
                this.pseudoPalindromicPaths( root.right );
            }

            this.pseudoPalindromicPaths( root.left );
        }

        this.arr[root.val]--;

        return this.ans;
    }
  
}
