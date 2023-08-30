import pandas as pd

def rearrange_products_table( products: pd.DataFrame ) -> pd.DataFrame:
    d = { "product_id": [], "store": [], "price": [] }
    def ap( i, j, k, d ):
        d["product_id"].append( i )
        d["store"].append( "store" + str( j ) )
        d["price"].append( k )
        
    for p, q in products.iterrows():
        for i in range( 1, 4 ):
            if q[i] is not pd.NA:
                ap( q[0], i, q[i], d )
            
    return pd.DataFrame( d )