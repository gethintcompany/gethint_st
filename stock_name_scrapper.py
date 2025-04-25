from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests

def get_good_stocks_S() -> list:


    driver = webdriver.Chrome()
    """Get 52 Week High from NSE"""
    url = "https://www.moneycontrol.com/stocks/marketstats/nsehigh/index.php"

    # initialize the Selenium Web Driver for Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # load and open the webpage
    driver.get(url)

    # load the entire webpage by going to its bottom
    select = driver.find_element(By.TAG_NAME, "body")
    for i in range(100):
        select.send_keys(Keys.PAGE_DOWN)

    nse_stocks = driver.find_element(By.CLASS_NAME, 'ReuseTable_PR__IANlW').text
    nse_stocks = nse_stocks.splitlines()
    temp = []
    for data, count in zip(nse_stocks, range(len(nse_stocks))):
        if count % 2 != 0:
            temp.append(data)
    good_stocks = temp


    """Get 52 Week High from BSE"""
    url = "https://www.moneycontrol.com/stocks/marketstats/bsehigh/index.php"
    driver.get(url)

    # load the entire webpage by going to its bottom
    select = driver.find_element(By.TAG_NAME, "body")
    for i in range(100):
        select.send_keys(Keys.PAGE_DOWN)

    stocks = driver.find_element(By.CLASS_NAME, 'ReuseTable_PR__IANlW').text
    stocks = stocks.splitlines()
    temp = []
    for data, count in zip(stocks, range(len(stocks))):
        if count % 2 != 0:
            temp.append(data)
    good_stocks += temp


    """Get Top Gainers from NSE"""
    url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
    driver.get(url)

    # load the entire webpage by going to its bottom
    select = driver.find_element(By.TAG_NAME, "body")
    for i in range(100):
        select.send_keys(Keys.PAGE_DOWN)
    stocks = driver.find_element(By.CSS_SELECTOR, "#mc_content > section > section > div.clearfix.stat_container > div.columnst.FR.wbg.brdwht > div > div > div.bsr_table.hist_tbl_hm").text
    stocks = stocks.splitlines()
    temp = []
    for data, count in zip(stocks, range(len(stocks))):
        if count % 2 != 0:
            temp.append(data)
    good_stocks += temp

    """Get Top Gainers from BSE"""
    url = "https://www.moneycontrol.com/stocks/marketstats/bsegainer/index.php"
    driver.get(url)

    # load the entire webpage by going to its bottom
    select = driver.find_element(By.TAG_NAME, "body")
    for i in range(100):
        select.send_keys(Keys.PAGE_DOWN)
    stocks = driver.find_element(By.CSS_SELECTOR, "#mc_content > section > section > div.clearfix.stat_container > div.columnst.FR.wbg.brdwht > div > div > div.bsr_table.hist_tbl_hm").text
    stocks = stocks.splitlines()
    temp = []
    for data, count in zip(stocks, range(len(stocks))):
        if count % 2 != 0:
            temp.append(data)
    good_stocks += temp

    driver.close()

    good_stocks = list(set(good_stocks))

    return good_stocks





def get_good_stocks_bs() -> list:
    companies_to_scrape_list = []
    URL_list = ["https://www.moneycontrol.com/stocks/marketstats/bsehigh/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/nsehigh/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/bsegainer/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/onlybuyers.php?optex=BSE&opttopic=buyers&sort=perchg",
                "https://www.moneycontrol.com/stocks/marketstats/onlybuyers.php",
                "https://www.moneycontrol.com/stocks/marketstats/bsemact1/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php",
                ]

    """         "https://www.moneycontrol.com/stocks/marketstats/bse_pshockers/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/nse_pshockers/index.php"
                "https://www.moneycontrol.com/stocks/marketstats/bse_vshockers/index.php",
                "https://www.moneycontrol.com/stocks/marketstats/nse_vshockers/index.php"""

    for URL in URL_list:
        response = requests.get(URL, timeout=20)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")

        table_tags = soup.find_all("a", target="_blank", style="color:#333")

        for company in table_tags:
            companies_to_scrape_list.append(str(company).split(">")[1].split("<")[0])

    companies_to_scrape_list = list(set(companies_to_scrape_list))
    print(companies_to_scrape_list)
    print(len(companies_to_scrape_list))
    return companies_to_scrape_list