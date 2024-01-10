public class Solution
{

    public static int beautifulIndex( int N, int[] A )
    {
        if ( N < 2 )
        {
            return N;
        }

        int[] p = new int[N];
        int[] q = new int[N];
        p[0] = A[0];
        q[ N - 1 ] = A[ N - 1 ];

        for ( int i = 1; i < N - 1; i++ )
        {
            p[i] = p[ i - 1 ] + A[i];
        }

        for ( int i = N - 2; i >= 0; i-- )
        {
            q[i] = q[ i + 1 ] + A[i];
        }

        if ( q[1] == 0 )
        {
            return 1;
        }

        for ( int i = 1; i < N - 1; i++ )
        {
            if ( p[ i - 1 ] == q[ i + 1 ] )
            {
                return i + 1;
            }
        }

        if ( p[ N - 2 ] == 0 )
        {
            return N;
        }

        return -1;
    }
}
