from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data_collection.config import *
from utils.data_utils import get_nse_isin_list

class MoneyControl():

    def __init__(self):
        driver = webdriver.Firefox()
        driver.get(money_control_home_url)
        driver.implicitly_wait(3)
        self.driver = driver


    def get_home_url_for_stocks(self, last_index=0):

        for stock in get_nse_isin_list()[last_index:]:
            self.ofile = open(money_control_urls_file, 'a')
            retry_search_box = 0
            try :
                search_box = self.driver.find_element_by_xpath('//input[@class="txtsrchbox FL"]')
            except:
                self.driver.back()
                print("could not find search box hence going back ")
                retry_search_box += 1
                if retry_search_box == 3:
                    break

            print("search_box displayed :",search_box.is_displayed())
            search_box.click()
            try:
                print("clearing Search box...")
                search_box.clear()
            except :
                self.driver.back()
                print("could not clear search box hence going back ")
                continue


            search_box.send_keys(stock)
            search_box.send_keys(Keys.ENTER)

            try :
                self.driver.switch_to.alert.accept()
            except :
                print("Handled alert exception...")
            try :
                no_match = self.driver.find_element_by_xpath("//p[text()=' Sorry, there are no matches for your search.']")
                if not no_match.is_displayed():
                    print("No match found for ", stock)
                    continue
            except:
                pass
            if 'compsearchnew' in str(self.driver.current_url):
                self.driver.back()
                continue
            try:
                sector = self.driver.find_element_by_xpath("//span[@class='hidden-lg']").get_attribute("innerHTML")
                f_ratios = self.driver.find_element_by_xpath("//a[@title='Financial Ratios']").get_attribute('href')
                pl_ratios = self.driver.find_element_by_xpath("//a[@title='Profit & loss']").get_attribute('href')
                q_ratios = self.driver.find_element_by_xpath("//a[@title='Quarterly Results']").get_attribute('href')
            except:
                print('error finding ratios element')
                self.driver.back()
                continue



            self.ofile.write(str(stock)+ delimiter +
                            str(sector) + delimiter +
                            f_ratios + delimiter +
                            pl_ratios + delimiter +
                            q_ratios +
                            '\n')


def get_last_stock_in_urls_file():
    stocks = get_nse_isin_list()
    try:
        with open(money_control_urls_file, 'r') as f:
            last_line = f.readlines()[-1]
            last_isin = last_line.split(delimiter)[0]
            last_index = stocks.index(last_isin)
        return last_index
    except:
        return 0


def run():
    index = get_last_stock_in_urls_file()
    mc = MoneyControl()
    mc.get_home_url_for_stocks(index)

if __name__ == "__main__":
    run()

