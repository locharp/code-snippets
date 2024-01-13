class Solution
{
    public int numberOfBeams( String[] bank )
    {
        int prev = 0;
        int curr = 0;
        int ans = 0;

        for ( String row : bank )
        {
            for ( char c : row.toCharArray() )
            {
                if ( c == '1' )
                {
                    curr++;
                }
            }
            
            if ( curr > 0 )
            {
                ans += prev * curr;
                prev = curr;
                curr = 0;
            }
        }

        return ans;
    }
}
