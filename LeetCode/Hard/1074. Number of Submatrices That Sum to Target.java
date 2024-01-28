class Solution
{
    
    ArrayList< ArrayList<Integer> > m;
    Integer ans;
    Integer t;
    
    
    
    Solution()
    {
        m = new ArrayList<>();
        ans = 0;
    }
    
    
    
    void e( int[][] m )
    {
        for ( int[] i : m )
        {
            ArrayList<Integer> r = new ArrayList<>();
            r.add( 0 );
            
            for ( int j : i )
            {
                r.add( j + r.get( r.size() - 1 ));
            }
            
            this.m.add( r );
        }
    }
    
    
    
    void f( int i, int j )
    {
        HashMap< Integer, Integer > a = new HashMap<>();
        a.put( 0, 1 );
        Integer k = 0;
        
        for ( var r : m )
        {
            k += r.get( j ) - r.get( i );
            ans += a.getOrDefault( k - t, 0 );
            a.put( k, a.getOrDefault( k, 0 ) + 1 );
        }
    }
    
    
    
    public int numSubmatrixSumTarget( int[][] matrix, int target )
    {
        t = target;
        e( matrix );
        int n = matrix[0].length;
        
        for ( int i = 0; i < n; i++ )
        {
            for ( int j = i + 1; j <= n; j++ )
            {
                f( i, j );
            }
        }
        
        return ans;
    }

}
