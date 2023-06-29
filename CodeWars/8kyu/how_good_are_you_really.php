function betterThanAverage( $classPoints, $yourPoints )
{
    if ( $yourPoints > array_sum( $classPoints ) / count( $classPoints ) )
    {
        return True;
    }
    else
    {
        return False;
    }
}