from os.path import join, dirname
import os

cur_dir = dirname(dirname(__file__))
collected_data = 'collected_data'
all_stock_ids_txt = "../collected_data/all_stock_ids.txt"
money_control_home_url = "https://www.moneycontrol.com/"
bse_stocks_file = join(cur_dir, collected_data+'/ListOfScrips.csv')
nse_stocks_file = join(cur_dir, collected_data+'/EQUITY_L.csv')
f_ratios_file = join(cur_dir, collected_data+'/f_ratios_list.txt')
money_control_urls_file = join(cur_dir, collected_data+'/money_control_urls.csv')
delimiter = '::'