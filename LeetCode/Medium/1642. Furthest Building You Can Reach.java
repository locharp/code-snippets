class Solution
{

    public int furthestBuilding
    ( int[] heights, int bricks, int ladders )
    {
        PriorityQueue< Integer > queue =
            new PriorityQueue<>();
        int i = 1;

        for ( ; i < heights.length; i++ )
        {
            int diff = heights[ i - 1 ] - heights[i];

            if ( diff >= 0 )
            {
                continue;
            }

            bricks += diff;
            queue.offer( diff );
            
            if ( bricks < 0 )
            {
                if ( ladders < 1 )
                {
                    break;
                }
                else
                {
                    ladders--;
                    bricks -= queue.poll();
                }
            }
        }

        return i - 1;
    }

}
