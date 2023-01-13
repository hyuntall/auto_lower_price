from selenium.webdriver.common.by import By

import request_naver
from bs4 import BeautifulSoup as bs
import requests
import main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
options.add_argument('user-agent=' + user_agent)
driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
logger = main.logger
HEADER ={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def getItemPrice(iteminfo):
    link = iteminfo.find_element(By.CSS_SELECTOR, '.basicList_link__JLQJf').get_attribute('href')
    price = iteminfo.find_element(By.CSS_SELECTOR, '.price_num__S2p_v').text
    try:
        delevery = iteminfo.find_element(By.CSS_SELECTOR, '.price_delivery__yw_We')
        delprice = delevery.text
    except:
        itemDetailPage = requests.get(link, headers=HEADER)
        deleveryPrice = bs(itemDetailPage.text, "html.parser").select_one('.productByMall_gift__oidOR')
        delprice = deleveryPrice.text
    return [price, delprice, link]

def get_mallName(mallList):
    print(mallList.text)
    try:
        mallName = mallList.find_element(By.CSS_SELECTOR, '.basicList_mall_list__S_B5C')
        return mallName.text
    except:
        try:
            mallName = mallList.find_element(By.CSS_SELECTOR,".basicList_mall_area__faH62 .basicList_mall_title__FDXX5 .basicList_mall__BC5Xu")
        except:
            print(1)
            return None
    return mallName.text


def scrap(name):
    URL = f"https://search.shopping.naver.com/search/all?frm=NVSHTTL&query={name}&sort=price_asc&sps=N"
    #page = requests.get(URL, headers=HEADER)
    #if page.status_code != 200:
    #    logger.error(f"{name}: 비정상적 요청으로 감지되었습니다.{page.status_code}")
    #    return [None, None, None, None]
    driver.get(URL)
    #soup = bs(page.text, "html.parser")
    #.noResultWithBestResults_no_keyword___Jhtn
    try:
        elements = driver.find_element(By.CSS_SELECTOR, '.basicList_item__0T9JD')
    except:
        logger.info(f"{name}: 검색 결과가 없습니다.")
        return [None, None, None, None]
    #elements = soup.select_one('.basicList_item__0T9JD')
    iteminfo = elements.find_element(By.CSS_SELECTOR, '.basicList_info_area__TWvzp')
    try:
        mallName = elements.find_element(By.CSS_SELECTOR, '.basicList_mall_list__S_B5C li:first-child .basicList_mall_name__XQlSa').text

    except:
        mallName = request_naver.get_lprice(name)[3]

    arr = getItemPrice(iteminfo)
    arr.append(mallName)
    #mallName = get_mallName(mallList)
    #if not mallName:
    #    mallName = request_naver.get_lprice(name)[3]
    #    #print(mallName)
    return arr

if __name__ == '__main__':
    print(scrap("AOJN7027M2"))