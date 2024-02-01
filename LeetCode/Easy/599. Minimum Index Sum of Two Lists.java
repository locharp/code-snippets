class Solution
{
    
    public String[] findRestaurant
    ( String[] list1, String[] list2 )
    {
        HashMap< String, Integer > map =
            new HashMap<>();
        TreeMap< Integer, ArrayList< String > > treeMap =
            new TreeMap<>();
        
        for ( int i = 0; i < list1.length; i++ )
        {
            map.put( list1[i], i );
        }
        
        for ( int i = 0; i < list2.length; i++ )
        {
            if ( map.containsKey( list2[i] ) )
            {
                int j = map.get( list2[i] ) + i;
                
                if ( !treeMap.containsKey( j ) )
                {
                    treeMap.put( j, new ArrayList<>() );
                }
                
                treeMap.get( j ).add( list2[i] );
            }
        }
        
        ArrayList< String > least =
            treeMap.firstEntry().getValue();
        String[] ans = new String[ least.size() ];
        
        for ( int i = 0; i < ans.length; i++ )
        {
            ans[i] = least.get( i );
        }
        
        return ans;
    }
    
}
