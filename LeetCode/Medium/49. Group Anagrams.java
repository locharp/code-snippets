class Solution
{
    
    public List< List< String > > groupAnagrams
    ( String[] strs )
    {
        HashMap< String, Integer > map =
            new HashMap<>();
        List< List< String > > ans =
            new ArrayList<>();
        
        for ( String str : strs )
        {
            char[] a = str.toCharArray();
            Arrays.sort( a );
            String s = new String( a );
            
            if ( map.containsKey( s ) )
            {
                ans.get( map.get( s ) ).add( str );
            }
            else
            {
                ans.add( new ArrayList<>() );
                ans.get( map.size() ).add( str );
                map.put( s, map.size() );
            }
        }
        
        return ans;
    }
    
}
