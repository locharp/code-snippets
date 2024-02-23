class Solution
{

    public int findCheapestPrice
    ( int n, int[][] flights, int src, int dst, int k )
    {
        HashMap< Integer, HashMap< Integer, Integer > > map =
            new HashMap<>();
        PriorityQueue< ArrayList< Integer > > queue =
            new PriorityQueue<>( ( x, y ) -> x.get( 0 ).compareTo( y.get( 0 ) ) );
        HashMap< Integer, Integer > visited =
            new HashMap<>();
        queue.offer( new ArrayList<>( List.of( 0, src, 0 ) ) );
        k++;

        for ( int[] flight : flights )
        {
            if ( !map.containsKey( flight[0] ) )
            {
                map.put( flight[0], new HashMap<>() );
            }

            map.get( flight[0] ).put( flight[1], flight[2] );
        }

        for ( int i = 0; i < n; i++ )
        {
            visited.put( i, k );
        }
        
        while ( !queue.isEmpty() )
        {
            ArrayList< Integer > curr = queue.poll();
            
            if ( curr.get( 1 ).equals( dst ) )
            {
                return curr.get( 0 );
            }
            else if ( visited.get( curr.get( 1 ) ).compareTo( curr.get( 2 ) ) <= 0
                || !map.containsKey( curr.get( 1 ) ) )
            {
                continue;
            }

            visited.put( curr.get( 1 ), curr.get( 2 ) );
            curr.set( 2, curr.get( 2 ) + 1 );

            for ( Map.Entry< Integer, Integer > flight : map.get( curr.get( 1 ) ).entrySet() )
            {
                ArrayList< Integer > arr = new ArrayList<>();
                arr.add( curr.get( 0 ) + flight.getValue() );
                arr.add( flight.getKey() );
                arr.add( curr.get( 2 ) );
                queue.offer( arr );
            }
        }

        return -1;
    }

}
