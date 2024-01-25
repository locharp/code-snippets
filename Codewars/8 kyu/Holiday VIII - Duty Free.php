<?php



function dutyFree( int $n, int $d, int $h ): int
{
    return floor( $h / ( $n * $d / 100 ) );
}



?>
