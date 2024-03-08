class Solution
{
    
    public int maxFrequencyElements
    ( int[] nums )
    {
        HashMap< Integer, Integer > map =
            new HashMap<>();
        
        
        for ( int num : nums )
        {
            map.put( num, map.getOrDefault( num, 0 ) + 1 );
        }
        
        
        ArrayList< Integer > list =
            new ArrayList<>( map.values() );
        Collections.sort( list, Collections.reverseOrder() );
        int ans = list.get( 0 );
        int max = list.get( 0 );
        
        
        for (int i = 1; i < list.size() && list.get( i ) == max; i++ )
        {
            ans += max;
        }
        
        
        return ans;
    }
    
}
