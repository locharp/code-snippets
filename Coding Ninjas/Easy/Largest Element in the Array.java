import java.util.stream.IntStream;

public class Solution
{

    static int largestElement( int[] arr, int n )
    {
        return IntStream.of( arr ).max().getAsInt();
    }
}
