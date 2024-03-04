class Solution
{

    public int bagOfTokensScore
    ( int[] tokens, int power )
    {
        ArrayDeque< Integer > deque = new ArrayDeque<>();
        Arrays.sort( tokens );
        int i = 0;
        int j = tokens.length - 1;
        int ans = 0;
        int totalPower = power;


        while ( i <= j )
        {
            if ( tokens[i] <= totalPower )
            {
                while ( power < tokens[i] )
                {
                    power += deque.poll();
                }
                

                totalPower -= tokens[i];
                power -= tokens[i++];
                ans++;
            }
            else if ( ans > 0 )
            {
                ans--;
                totalPower += tokens[j];
                deque.offer( tokens[j--] );
            }
            else
            {
                break;
            }
        }


        return ans + deque.size();
    }

}
