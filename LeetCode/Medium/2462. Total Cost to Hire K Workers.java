class Solution
{
    public long totalCost( int[] costs, int k, int candidates )
    {
        int len = costs.length;

        if ( len == 1 )
        {
            return costs[0];
        }
        else if ( len <= k )
        {
            return IntStream.of( costs ).mapToLong( i -> i ).sum();
        }

        int mid = ( len + 1 ) / 2;

        ArrayList<Integer> pool = new ArrayList( Arrays.stream( costs ).boxed().collect( Collectors.toList() ) );

        PriorityQueue<Integer> first = new PriorityQueue<>();
        PriorityQueue<Integer> last = new PriorityQueue<>();

        for ( int i = 0; i < Math.min( candidates, mid ); i++ )
        {
            first.add( pool.remove( 0 ) );
        }

        for ( int i = 0; i < Math.min( candidates, len - mid ); i++ )
        {
            last.add( pool.remove( pool.size() - 1 ) );
        }

        first.add(Integer.MAX_VALUE);
        last.add(Integer.MAX_VALUE);

        Integer min1 = first.poll();
        Integer min2 = last.poll();
        long cost = 0;

        while ( k-- > 0 )
        {
            if ( min1 <= min2 )
            {
                cost += min1;
                
                if ( !pool.isEmpty() )
                {
                    first.add( pool.remove( 0 ) );
                }

                if ( first.isEmpty() )
                {
                    break;
                }

                min1 = first.poll();
            }
            else
            {
                cost += min2;
                
                if ( !pool.isEmpty() )
                {
                    last.add( pool.remove( pool.size() - 1 ) );
                }

                if ( last.isEmpty() )
                {
                    break;
                }

                min2 = last.poll();
            }
        }

        while ( k > 0 && !first.isEmpty() )
        {
            cost += min1;
            min1 = first.poll();
            k--;
        }

        while ( k > 0 && !last.isEmpty() )
        {
            cost += min2;
            min2 = last.poll();
            k--;
        }

        return cost;
    }
}