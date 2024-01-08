<?php



class Solution
{
    function __construct()
    {
        $this->ans = 0;
    }



    function rangeSumBST( $root, $low, $high )
    {
        if ( !isset( $root ) )
        {
            return $this->ans;
        }

        if ( $root->val > $low )
        {
            $this->rangeSumBST( $root->left, $low, $high );
        }

        if ( $root->val < $high )
        {
            $this->rangeSumBST( $root->right, $low, $high );
        }

        if ( $root->val >= $low && $root->val <= $high )
        {
            $this->ans += $root->val;
        }

        return $this->ans;
    }
}



?>
