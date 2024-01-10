<?php



class Solution
{
    
    function f( $root, &$arr )
    {
        if ( $root == NULL )
        {
            return;
        }
        else if ( $root->left != NULL )
        {
            $this->f ( $root->left, $arr );
            
            if ( $root->right != NULL )
            {
                $this->f( $root->right, $arr );
            }
        }
        else if ( $root->right != NULL )
        {
            $this->f( $root->right, $arr );
        }
        else
        {
            array_push( $arr, $root->val );
        }
    }
    
    
    
    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    
    function leafSimilar( $root1, $root2 )
    {
        $a1 = array();
        $a2 = array();
        $this->f( $root1, $a1 );
        $this->f( $root2, $a2 );
        
        return $a1 == $a2;
    }
}



?>
