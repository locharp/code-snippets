class Solution
{

    public int longestCommonSubsequence( String text1, String text2 )
    {
        if ( text1.length() < text2.length() )
        {
            return longestCommonSubsequence( text2, text1 );
        }
        
        int n = text2.length() + 1;
        int[] p = new int[n];

        for ( int i = 0; i < text1.length(); i++ )
        {
            int[] q = new int[n];

            for( int j = 1; j < n; j++ )
            {
                if ( text1.charAt( i ) == text2.charAt( j - 1 ) )
                {
                    q[j] = p[ j - 1 ] + 1;
                }
                else
                {
                    q[j] = Math.max( p[j], q[ j - 1 ] );
                }
                
            }
            
            p = q;
        }
        
        return p[ n - 1 ];
    }

}
