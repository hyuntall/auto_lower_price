import urllib.parse
import requests
import json

CLIENT_ID = "gCoWAOgsc_VjbgJdnSLP"  # 이거 일단 내 네이버 계정으로 발급받은 키인데 나중에 서윤이 네이버 계정으로 발급 받는 방법 알려줄게
CLIENT_PASSWORD = "AB9p7GeLG5"
HEADER = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_PASSWORD,
}


def request_api(name):
    # Open API 검색 요청 개체 설정
    url = "https://openapi.naver.com/v1/search/shop.json"
    option = "&display=1&sort=count"
    query = "?query=" + urllib.parse.quote(name)
    url_query = url + query + option
    # 검색 요청 및 처리
    response = requests.get(url_query, headers=HEADER)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return json_data
    return None


def get_lprice(name):
    json_data = request_api(name)
    if json_data:
        items = json_data['items']
        if items:
            title = items[0]['title']
            lprice = items[0]['lprice']
            link = items[0]['link']
            mallName = items[0]['mallName']
            return [title, lprice, link, mallName]
    else:  # 검색 정보가 없을 경우 None 리턴
        return [None, None, None, None]


if __name__ == "__main__":
    get_lprice("COLU6051W1")
