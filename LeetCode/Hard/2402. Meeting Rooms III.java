import java.util.AbstractMap.*;

class Solution
{

    public int mostBooked
    ( int n, int[][] meetings )
    {
        PriorityQueue< SimpleImmutableEntry< Long, Integer > > used =
            new PriorityQueue<>( new RoomComparator() );
        PriorityQueue< Integer > unused =
            new PriorityQueue<>();
        int counts[] = new int[n];
        int ans = 0;
        int max = -1;
        int start = 0;
        long end = 0;
        int room = 0;
        Arrays.sort( meetings, Comparator.comparingInt( x -> x[0] ) );
        
        for ( int i = 0; i < n; i++ )
        {
            unused.offer( i );
        }

        for ( int[] meeting : meetings )
        {
            start = meeting[0];
            end = meeting[1];

            while ( !used.isEmpty()
                && used.peek().getKey() <= start )
            {
                unused.offer( used.poll().getValue() );
            }

            if ( unused.isEmpty() )
            {
                end += used.peek().getKey() - start;
                room = used.poll().getValue();
            }
            else
            {
                room = unused.poll();
            }
            
            used.offer( new SimpleImmutableEntry<>( end, room ) );
            counts[room]++;
        }
        
        for ( int i = 0; i < n; i++ )
        {
            if ( counts[i] > max )
            {
                ans = i;
                max = counts[i];
            }
        }

        return ans;
    }

}





class RoomComparator implements Comparator< SimpleImmutableEntry< Long, Integer > >
{

    @Override
    public int compare
    ( SimpleImmutableEntry< Long, Integer > x,
      SimpleImmutableEntry< Long, Integer > y )
    {
        if ( x.getKey().equals( y.getKey() ) )
        {
            return Integer.compare( x.getValue(), y.getValue() );
        }
        else
        {
            return Long.compare( x.getKey(), y.getKey() );
        }
    }

}
