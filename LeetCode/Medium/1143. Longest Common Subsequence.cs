public class Solution
{

    public int LongestCommonSubsequence( string text1, string text2 )
    {
        if ( text1.Length < text2.Length )
        {
            return LongestCommonSubsequence( text2, text1 );
        }
        
        int n = text2.Length + 1;
        int[] p = new int[n];

        for ( int i = 0; i < text1.Length; i++ )
        {
            int[] q = new int[n];

            for( int j = 1; j < n; j++ )
            {
                if ( text1[i] == text2[ j - 1 ] )
                {
                    q[j] = p[ j - 1 ] + 1;
                }
                else
                {
                    q[j] = Math.Max( p[j], q[ j - 1 ] );
                }
                
            }
            
            p = q;
        }
        
        return p[ n - 1 ];
    }

}
