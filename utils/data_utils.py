import pandas as pd
from data_collection.config import *
# bse_df = pd.read_csv(bse_stocks_file)

def get_nse_isin_list():
    nse_df = pd.read_csv(nse_stocks_file)
    return list(nse_df[' ISIN NUMBER'].to_list())
