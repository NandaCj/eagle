from config import (market_on_mobile_url, all_stock_ids_txt)
from utils.request_utils import (read_url)
from utils.file_io_utils import re_write_file

text_data = read_url(market_on_mobile_url)
re_write_file(all_stock_ids_txt, text_data)




