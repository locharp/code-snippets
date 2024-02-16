class Solution
{

    public int findLeastNumOfUniqueInts
    ( int[] arr, int k )
    {
        HashMap< Integer, Integer > map =
            new HashMap<>();
            
        for ( int i : arr )
        {
            map.put( i, map.getOrDefault( i, 0 ) + 1);
        }
        
        PriorityQueue< Integer > queue =
            new PriorityQueue<>( map.values() );
        int ans = map.size();
        
        while ( !queue.isEmpty() )
        {
            k -= queue.poll();
            
            if ( k >= 0 )
            {
                ans--;
            }
            else
            {
                break;
            }
        }
        
        return ans;
    }
    
}
