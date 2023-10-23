function grow( $a )
{
    $product = 1;
  
    foreach ( $a as $num )
    {
        $product *= $num;
    }
  
    return $product;
}