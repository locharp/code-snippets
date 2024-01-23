<?php



function removeRotten( $fruitBasket )
{
    if ( !isset( $fruitBasket ) )
    {
        return [];
    }
        
    for ( $i = 0; $i < count( $fruitBasket ); $i++ )
    {
        if ( str_starts_with( $fruitBasket[$i], "rotten" ) )
        {
            $fruitBasket[$i] = substr_replace( $fruitBasket[$i], strtolower( $fruitBasket[$i][6] ), 0, 7 );
        }
    }
    
    return $fruitBasket;
}



?>
