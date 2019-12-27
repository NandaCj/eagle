import requests
from bs4 import BeautifulSoup
import re
import sys
sys.path.append('/home/nandagopal/eagle')
from data_collection.config import *

f_ratios_list = list(open(f_ratios_file, 'r').readlines())


def find_data_for_all_stock(sector=None):
    """
    method to be called from airflow

    loops through all urls and get their financial ratios

    :return:
    """
    for url in open(money_control_urls_file, 'r').readlines():
        if sector in url :
            find_data(url)



def find_data(url):
    """

    :param url: finace ration url of money control for single stock
    :return:

    INE428A01015,Basic EPS,-65.34,  -59.63,  -4.36,  -12.68,  11.39
    INE428A01015,Diluted Eps,-65.34,  -59.63,  -4.36,  -12.68,  11.39
    INE428A01015,Cash EPS,-39.09,  -53.69,  -2.11,  -10.21,  12.61

    """
    ofile = open(finance_csv, 'a')
    isin, sector, f_ratios, pl_ratios, q_ratios = url.split(delimiter)
    url = f_ratios
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
                        ratios.append(re.findall(r'-?\d+.\d+',str(data))[0])
                    print(ratios)
                    ofile.write(isin + ',' + f_ratio +"," +",  ".join(ratios) + '\n')
            idx += 1
        except Exception as err:
            print(err)

find_data_for_all_stock('Banks - Public Sector')