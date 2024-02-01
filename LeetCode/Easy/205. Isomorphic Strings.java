class Solution
{
    
    public boolean isIsomorphic
    ( String s, String t )
    {
        HashMap< Character, Character > map =
            new HashMap<>();
        
        for ( int i = 0; i < s.length(); i ++ )
        {
            char u = s.charAt( i );
            char v = t.charAt( i );
            
            if ( map.containsKey( u ) )
            {
                if ( map.get( u ) != v )
                {
                    return false;
                }
            }
            else if ( map.containsValue( v ) )
            {
                return false;
            }
            
            map.put( u, v );
        }
        
        return true;
    }
    
}
