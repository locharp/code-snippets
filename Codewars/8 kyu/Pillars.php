<?php



function pillars( $numberOfPillars, $dist, $width )
{
    if ( $numberOfPillars < 2 )
    {
        return 0;
    }
  
    return ( ( $numberOfPillars - 1 ) * $dist * 100 ) + ( ( $numberOfPillars - 2 ) * $width );
}



?>
