import request_naver
import scrap_naver
import pandas as pd
import time

start = time.time()
data = pd.read_csv('tnd_itemName.csv', encoding='cp949', header=None, names=["name"])
df1 = pd.DataFrame(data)
item_list = []
cnt = 0
for name in df1['name']:
    try:
        scrap_naver.scrap(name)
        # item_list.append(request_naver.get_lprice(name))
    except Exception as e:
        print(f"{name}: {e}")
        item_list.append([None, None, None, None])
    cnt += 1

df2 = pd.DataFrame(item_list, columns=["title", "lprice", "link", "mallName"])
df3 = pd.concat([df1, df2], axis=1)
df3.to_csv('result2.csv', index=False, encoding="utf-8-sig")
end = time.time()
# 상품 최저가 , 무료배송(여부), 사이트이름,사이트 url(가능하면)
print(f"{end - start:.5f} sec")
