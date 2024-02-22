class Solution
{

    public int findJudge
    ( int n, int[][] trust )
    {
        int[][] people = new int[ n + 1 ][2];
        int m = n - 1;

        for ( int[] t : trust )
        {
            people[ t[0] ][0]++;
            people[ t[1] ][1]++;
        }
        
        for ( int i = 1; i <= n; i++ )
        {
            if ( people[i][0] < 1 && people[i][1] == m )
            {
                return i;
            }
        }

        return -1;
    }

}
