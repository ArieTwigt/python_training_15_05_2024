from typing import List, Dict
import pandas as pd
from utils import DEFAULT_COLUMNS, DEFAULT_COLUMN_NAMES

def convert_clean_list_to_df(items_list: List[Dict],  *args: str, **kwargs) -> pd.DataFrame:
    '''
    Converts the list with dictionaries to a pandas DataFrame.
    
    Applies data cleaning:
    * sub-selection of columns
    * renaming of columns
    * conversion to right data types
    * remove strange values

    input:
    * items_list: list with dictionaries

    output:
    * pandas DataFrame
    
    '''
    
    # conver the list to a dictionary
    df = pd.DataFrame(items_list)


    # sub-selection of columns
    selected_columns = DEFAULT_COLUMNS + list(args)

    # check for each value in the args, if it is present in the DataFrame
    #selected_columns_filtered = [column for column in selected_columns if column in df.columns]

    selected_columns_filtered = []

    for column in selected_columns:
        if column in df.columns:
            selected_columns_filtered.append(column)
        else:
            raise ValueError(f"The column '{column}' is not in the DataFrame")

    # update the column names
    DEFAULT_COLUMN_NAMES.update(kwargs)

    # modify the dataset
    df_subset = (df[selected_columns_filtered]
                 .rename(columns=DEFAULT_COLUMN_NAMES)
                 .dropna(subset=['aantal_cilinders', 'catalogusprijs'])
                 .assign(catalogusprijs = lambda x: x['catalogusprijs'].astype(float))
                 .assign(aantal_cilinders = lambda x: x['aantal_cilinders'].astype(int) )
                 .query("catalogusprijs <= 50000")
                 .sort_values(by="catalogusprijs", ascending=False)
    )
    
    return df_subset
