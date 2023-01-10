import urllib.parse
import requests
import json

CLIENT_ID = "gCoWAOgsc_VjbgJdnSLP"
CLIENT_PASSWORD = "AB9p7GeLG5"
HEADER = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_PASSWORD,
}

def get_lprice(name):
    url = "https://openapi.naver.com/v1/search/shop.json"
    option = "&display=1&sort=count"
    query = "?query=" + urllib.parse.quote(name)
    url_query = url + query + option

    # Open API 검색 요청 개체 설정
    response = requests.get(url_query, headers=HEADER)
    #검색 요청 및 처리
    rescode = response.status_code
    arr = []
    if(rescode == 200):
        json_data = json.loads(response.text)
        items = json_data['items']
        if items:
            title = items[0]['title']
            lprice = items[0]['lprice']
            link = items[0]['link']
            mallName = items[0]['mallName']
        else:
            title = None
            lprice = None
            link = None
            mallName = None
        arr.append(title)
        arr.append(lprice)
        arr.append(link)
        arr.append(mallName)
        # print(f"{title}: {lprice}원, {link}, {mallName}")
    else:
        print("Error code:"+rescode)
    return arr


if __name__ == "__main__":
    get_lprice("COLU6051W1")