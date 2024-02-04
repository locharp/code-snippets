class Solution
{
    
    HashMap< Character, Integer > map;
    int c, i, j, m, n, u, v;
    char[] o;
    
    
    Solution()
    {
        map = new HashMap<>();
        c = Integer.MAX_VALUE;
        i = 0;
        j = -1;
    }
    
    
    
    public String minWindow
    ( String s, String t )
    {
        m = s.length();
        n = t.length();
        o = s.toCharArray();
       
        for ( char ch : t.toCharArray() )
        {
            map.put( ch, map.getOrDefault( ch, 0 ) + 1 );
        }
        
        while ( n > 0 )
        {
            f();
            
            if( j == m )
            {
                return "";
            }
            else
            {
                if ( map.get( o[j] ) >= 0 )
                {
                    n--;
                }
            }
        }
        
        while ( j < m )
        {
            g();
            
            if ( j - i < c )
            {
                c = j - i;
                u = i;
                v = j;
            }
            
            f();
        }
        
        return s.substring( u, v + 1 );
    }
    
    
    
    void f()
    {
        while( ++j < m )
        {
            if ( map.containsKey( o[j] ) )
            {
                map.put( o[j], map.get( o[j] ) - 1 );
                return;
            }
        }
    }
    
    
    
    void g()
    {
        while ( i < j )
        {
            if ( map.containsKey( o[i] ) )
            {
                if ( map.get( o[i] ) < 0 )
                {
                    map.put( o[i], map.get( o[i] ) + 1 );
                }
                else
                {
                    return;
                }
            }
            
            i++;
        }
    }
    
}
