class Solution
{
    
    public List< Integer > findAllPeople
    ( int n, int[][] meetings, int firstPerson )
    {
        Arrays.sort( meetings, ( x, y ) -> x[2] - y[2] );
        UnionFind uf = new UnionFind( n );
        uf.unite( 0, firstPerson );
        
        for ( int i = 0, j = 1;
            i < meetings.length;
            j++ )
        {
            while ( j < meetings.length
                && meetings[j][2] == meetings[ j - 1 ][2] )
            {
                j++;
            }
            
            for ( int k = i; k < j; k++ )
            {
                uf.unite( meetings[k][0], meetings[k][1] );
            }
            
            for ( ; i < j; i++ )
            {
                uf.check( meetings[i][0] );
                uf.check( meetings[i][1] );
            }
        }
        
        return uf.toList();
    }
    
}





class UnionFind
{

    int[] roots;
    int[] levels;



    UnionFind( int n ) {
        roots = new int[n];
        levels = new int[n];
        
        for ( int i = 1; i < n; i++ )
        {
            roots[i] = i;
        }
    }



    void check( int x )
    {
        find( 0 );
        
        if( find( x ) != roots[0] )
        {
            roots[x] = x;
            levels[x] = 0;
        }
    }



    int find( int x )
    {
        if ( roots[x] != x )
        {
            roots[x] = find( roots[x] );
        }
        
        return roots[x];
    }



    void unite
    ( int x, int y )
    {
        int root_x = find( x );
        int root_y = find( y );
        
        if ( root_x == root_y )
        {
            return;
        }
        
        if ( levels[x] > levels[y] )
        {
            roots[root_y] = root_x;
        }
        else if ( levels[y] > levels[x] )
        {
            roots[root_x] = root_y;
        }
        else
        {
            roots[root_y] = root_x;
            levels[root_x]++;
        }
    }



    ArrayList< Integer > toList()
    {
        ArrayList< Integer > ans = new ArrayList<>();
        find( 0 );
        
        for ( int i = 0; i < roots.length; i++ )
        {
            if ( find( i ) == roots[0] )
            {
                ans.add( i );
            }
        }
        
        return ans;
    }
    
}
