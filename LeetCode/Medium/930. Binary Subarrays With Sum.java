class Solution
{
    
    public int numSubarraysWithSum
    ( int[] nums, int goal )
    {
        HashMap< Integer, Integer > map =
            new HashMap<>();
        int ans = 0;
        int count = 0;
        
        
        for ( int num : nums )
        {
            count += num;
            
            
            if ( count == goal )
            {
                ans++;
            }
            
         
            ans += map.getOrDefault( count - goal, 0 );
            map.put( count, map.getOrDefault( count, 0 ) + 1 );
        }
        
        
        return ans;
    }
    
}
