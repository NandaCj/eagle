import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append('/home/nandagopal/eagle')
from data_collection.config import *

f_ratios_list = list(open(f_ratios_file, 'r').readlines())


def find_data_for_all_stock():
    for url in open(money_control_urls_file, 'r').readlines():
        find_data(url)



def find_data(url):
    isin = url[:13]
    url = url[13:]
    print(isin, url)
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    td_list = list(soup.find_all('td'))
    idx = 0
    for ele in td_list:
        ele = str(ele)
        try:
            for f_ratio in f_ratios_list:
                f_ratio = f_ratio.rstrip('\n')
                if f_ratio in ele :
                    print(f_ratio)
                    ratios = []
                    for i in range(1, 6):
                        data = td_list[idx+i]
                        # print(data)
                        ratios.append(re.findall(r'\d+.\d+',str(data))[0])
            print(isin, ",".join(ratios))
            idx += 1
        except Exception as err:
            print(err)

find_data_for_all_stock()