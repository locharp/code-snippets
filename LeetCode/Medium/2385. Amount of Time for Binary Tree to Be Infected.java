class Solution
{

    HashMap< Integer, ArrayList<Integer> > graph;
    HashSet<Integer> infected;
    int ans;



    Solution()
    {
        this.graph = new HashMap<>();
        this.infected = new HashSet<>();
        this.ans = 0;
    }



    void draw( TreeNode root, TreeNode p )
    {
        if ( root == null )
        {
            return;
        }

        this.graph.put( root.val, new ArrayList<>() );
        this.graph.get( p.val ).add( root.val );
        this.graph.get( root.val ).add( p.val );
        this.draw( root.left, root );
        this.draw( root.right, root );
    }
    
    

    void infect( Integer start, int minute )
    {
        this.infected.add( start );
        this.ans = Math.max( this.ans, minute );
        
        for ( Integer next: this.graph.get( start ) )
        {
            if ( !this.infected.contains( next ) )
            {
                this.infect( next, minute + 1 );
            }
        }
    }


    
    public int amountOfTime( TreeNode root, int start )
    {
        
        this.graph.put( root.val, new ArrayList<>() );
        this.draw( root.left, root );
        this.draw( root.right, root );
        this.infect( start, 0 );

        return this.ans;
    }
}
