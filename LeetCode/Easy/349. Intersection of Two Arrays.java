class Solution
{
    
    public int[] intersection( int[] nums1, int[] nums2 )
    {
        Set<Integer> s1 = IntStream.of( nums1 ).boxed().collect( Collectors.toSet() );
        Set<Integer> s2 = IntStream.of( nums2 ).boxed().collect( Collectors.toSet() );
        s1.retainAll( s2 );
        
        return s1.stream().mapToInt( Integer::intValue ).toArray();
    }
    
}
