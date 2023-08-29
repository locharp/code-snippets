import pandas as pd

def count_rich_customers( store: pd.DataFrame ) -> pd.DataFrame:
    return pd.DataFrame( { "rich_count": [ len( store[ store["amount"] > 500 ].groupby( "customer_id" ) ) ] } )