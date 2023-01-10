from bs4 import BeautifulSoup as bs
import requests

HEADER ={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def getItemPrice(iteminfo):
    link = iteminfo.select_one('.basicList_link__JLQJf')['href']
    price = iteminfo.select_one('.price_num__S2p_v').text
    delevery = iteminfo.select_one('.price_delivery__yw_We')
    #print(price)
    if delevery:
        delprice = delevery.text
        #print(delevery.text)
    else:
        itemDetailPage = requests.get(link,headers=HEADER)
        deleveryPrice = bs(itemDetailPage.text, "html.parser").select_one('.productByMall_gift__oidOR')
        delprice = deleveryPrice.text
        #print(deleveryPrice.text)
    #if not delevery:
    #    print(delevery)
    #    itemPage = requests.get(link)
    #    delPrice = bs(itemPage.text, "html.parser").select_one('#__next > div > div.style_container__D_mqP > div.style_inner__ZMO5R > div.style_content_wrap__78pql > div.style_content__v25xx > div > div.summary_info_area__NP6l5 > div.condition_area > table > tbody > tr:nth-child(1) > td.productByMall_gift__oidOR')
    #    print(delPrice.text[:-1])

    return [price, delprice]

def get_mallName(mallList):
    print(mallList)

def scrap(name):
    print(name)
    #name = "COLU6051W1"
    URL = f"https://search.shopping.naver.com/search/all?frm=NVSHTTL&query={name}&sort=price_asc&sps=N"
    # URL = f"https://search.shopping.naver.com/search/all?query={name}&frm=NVSHATC"
    page = requests.get(URL, headers=HEADER)
    soup = bs(page.text, "html.parser")
    elements = soup.select_one('.basicList_item__0T9JD')
    print(URL)
    if not elements:
        return
    iteminfo = elements.select_one('.basicList_info_area__TWvzp')
    mallList = elements.select_one('.basicList_mall_area__faH62')
    arr = getItemPrice(iteminfo)
    print(arr)
    # print(elements[0])
    #for element in elements:
    #    price = element.select('#__next > div > div.style_container__UxP6u > div > div.style_content_wrap__Cdqnl > div.style_content__xWg5l > ul > div > div:nth-child(1) > li > div > div.basicList_info_area__TWvzp > div.basicList_price_area__K7DDT > strong > span > span.price_num__S2p_v')
    #    print(price[0].text)
    #    delivery = element.select('#__next > div > div.style_container__UxP6u > div > div.style_content_wrap__Cdqnl > div.style_content__xWg5l > ul > div > div:nth-child(2) > li > div > div.basicList_info_area__TWvzp > div.basicList_price_area__K7DDT > strong > span > span.price_delivery__yw_We')
    #    print(delivery)

if __name__ == '__main__':
    scrap("APYE8169F0")