<?php



function bump
( $x )
{
    if( substr_count( $x, "n" ) < 16 )
    {
        return "Woohoo!";
    }
    else
    {
        return "Car Dead";
    }
}



?>
