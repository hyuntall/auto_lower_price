import request_naver
import win32api
import scrap_naver
import pandas as pd
import time
import configparser
import logging
from tqdm import tqdm
import random

logging.basicConfig(level='INFO', filename='LogFile.log', encoding='utf-8')
logger = logging.getLogger('log')
config = configparser.ConfigParser()
config.read('config.ini', encoding='cp949')
def main():
    input = config['ETC']['INPUT_FILE']
    win32api.MessageBox(0, "상품 최저가 리스트 업데이트를 시작합니다.", "서윤", 0)
    logger.info("프로그램 시작")
    start = time.time()
    try:
        data = pd.read_csv(input, encoding='cp949', header=None, names=["name"])
    except:
        win32api.MessageBox(0, f"{input} 파일이 존재하지 않습니다.", "서윤", 0)
        logger.error(f"{input} 파일이 존재하지 않습니다.")
        exit()
    df1 = pd.DataFrame(data)
    item_list = []
    logger.info("csv 파일 읽기 완료")

    logger.info("상품 별 네이버 데이터 호출 시작")
    for name in tqdm(df1['name']):
        try:
            item_list.append(scrap_naver.scrap(name))
            #item_list.append(request_naver.get_lprice(name))
        except Exception as e:
            logger.error(f"{name} 오류: {e}")
            item_list.append([None, None, None, None])
        time.sleep(random.uniform(2, 4))

    logger.info("모든 상품 호출 완료")
    end = time.time()
    logger.info(f"현재 소요 시간: {end - start:.5f} sec")
    df2 = pd.DataFrame(item_list, columns=["lowest price", "shipping fee", "link", "mallName"])
    df3 = pd.concat([df1, df2], axis=1)
    df3.to_csv('result3.csv', index=False, encoding="utf-8-sig")
    logger.info("상품 별 최저가 업데이트 완료")
    end = time.time()
    logger.info(f"전체 소요 시간: {end - start:.5f} sec")
    win32api.MessageBox(0, "상품 최저가 리스트 업데이트가 완료되었습니다.", "서윤", 0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.info(e)