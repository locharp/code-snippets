class Solution
{
    public int findContentChildren( int[] g, int[] s )
    {
        Arrays.sort( g );
        Arrays.sort( s );
        int i = 0;
        int ans = 0;

        for ( int j : g )
        {
            while ( i < s.length && s[i] < j )
            {
                i++;
            }
            
            if ( i < s.length )
            {
                i++;
                ans++;
            }
            else
            {
                break;
            }
        }

        return ans;
    }
}
