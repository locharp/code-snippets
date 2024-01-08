<?php



function movie( $card, $ticket, $perc )
{
    $ans = $t = 0;
    $c = $card;
    $d = $ticket;
    
    while ( ceil( $c ) >= $t )
    {
        $ans++;
        $d *= $perc;
        $c += $d;
        $t += $ticket;
    }
    
    return $ans;
}



?>
