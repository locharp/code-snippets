<?php




function excludingVatPrice
( $price )
{
    if ( $price == null )
    {
        return -1;
    }
      else
    {
        return round( $price / 1.15, 2 );
    }
}



?>
