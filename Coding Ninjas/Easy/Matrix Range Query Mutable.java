import java.util.*;

public class Solution
{

    public static int[] matrixRangeSum
    ( int[][] grid, int[][] queries )
    {
        ArrayList< Integer > list = new ArrayList<>();
        int[][] a = new int[ grid.length ][ grid[0].length + 1 ];


        for ( int i = 0; i < a.length; i++ )
        {
            for ( int j = 0; j < grid[0].length; j++ )
            {
                a[i][ j + 1 ] = a[i][j] + grid[i][j];
            }
        }


        for ( int[] query : queries )
        {
            if ( query[0] > 1 )
            {
                int d = query[3] - grid[ query[1] ][ query[2] ];
                grid[ query[1] ][ query[2] ] = query[3];


                for ( int i = query[2] + 1; i < a[0].length; i++ )
                {
                    a[ query[1] ][i] += d;
                }
            }
            else
            {
                int sum = 0;


                for ( int i = query[1]; i <= query[3]; i++ )
                {
                    sum += a[i][ query[4] + 1 ] - a[i][ query[2] ];
                }


                list.add( sum );
            }
        }


        return list.stream().mapToInt( Integer::intValue ).toArray();
    }

}
