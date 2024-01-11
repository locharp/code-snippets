<?php



class Solution
{
    
    function f( $root, $m, $n )
    {
        if ( $root == Null )
        {
            return 0;
        }
        
        $m = max( $m, $root->val );
        $n = min( $n, $root->val );
        
        return max( $m - $n, $this->f( $root->left, $m, $n ), $this->f( $root->right, $m, $n ) );
    }
    
    
    
    function maxAncestorDiff( $root )
    {
        return $this->f( $root, $root->val, $root->val );;
    }
    
}



?>
