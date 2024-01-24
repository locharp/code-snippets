import java.util.stream.*;

public class Solution
{
    public static int removeDuplicates( int[] arr,int n )
    {
        return IntStream.of( arr ).boxed().collect( Collectors.toSet() ).size();
    }
}
