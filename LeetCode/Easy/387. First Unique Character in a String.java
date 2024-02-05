class Solution
{

    public int firstUniqChar
    ( String s )
    {
        HashMap< Character, Integer > map =
            new HashMap<>();
        HashSet< Character > set =
            new HashSet<>();
        int ans = s.length();

        for ( int i = 0; i < s.length(); i++ )
        {
            if ( set.contains( s.charAt( i ) ) )
            {
                map.remove( s.charAt( i ) );
            }
            else
            {
                set.add( s.charAt( i ) );
                map.put( s.charAt( i ), i );
            }
        }

        for ( Integer i : map.values() )
        {
            ans = Math.min( i, ans );
        }

        if ( ans == s.length() )
        {
            return -1;
        }
        else
        {
            return ans;
        }
    }

}
