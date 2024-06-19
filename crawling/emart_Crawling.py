import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 필요하면 경로 수정
file = r"C:\Users\HOME\Downloads\repurve_data.xlsx"

df = pd.read_excel(file, sheet_name = 2, usecols = 'E')

driver = webdriver.Chrome()

product_size = []
product_image = []
real_product_name = []
big_cate = []
middle_cate = []
small_cate = []
c = None
c2 = None

# Process
# 이마트몰에서 해당 상품 검색


for index, row in df.iloc[1330:1335].iterrows():
    i = row['상품명']
    search_url = f"https://emart.ssg.com/search.ssg?target=all&query={i}"
    site = driver.get(search_url)
    time.sleep(random.uniform(5, 10))

    not_search_emart = None  # Initialize not_search_emart here

    try:
        not_search_emart = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/p').text
    except:
        print()

    # 이마트에서 검색이 안 되는 제품을 다나와에서 검색
    if not_search_emart:
        try:
            danawa_url = f"https://search.danawa.com/dsearch.php?query={i}"
            site = driver.get(danawa_url)
            time.sleep(random.uniform(5, 10))
        except:
            print("danawa_homepage_error")

        # [error1] - 2글자 이하로 검색시 나오는 문구
        try:
            danawa_not_search1 = driver.find_element(By.ID, 'nosearchArea')
        except:
            danawa_not_search1 = []
    
        # [error2] - 상품을 찾을 수 없을 때 나오는 문구
        try:
            danawa_not_search2 = driver.find_element(By.XPATH, '//*[@id="nosearchArea"]/div/ul')
        except:
            danawa_not_search2 = []
            
        # Case1-1. 해당 상품이 없을 경우 (X) -> 다나와 검색 -> 해당 상품이 있으면 (O) 상품명, 상세정보 전부 가져오기(특정 크기를 가져오는 경우의 수보다 더 많기 때문)
        # Case1-2. 해당 상품이 없을 경우 (X) -> 다나와 검색 -> 해당 상품이 없으면 (X) None을 가져옴
        if danawa_not_search1 or danawa_not_search2:
            real_product_name.append(f"{i}_notsearch")
            print("!!!!!!")
            product_size.append(f"none_danawa")
        else:
            danawa_click_name1 = driver.find_element(By.CLASS_NAME, 'prod_name').text
            real_product_name.append(f"{i}_{danawa_click_name1}")
    
            try:
                danawa_size1 = driver.find_element(By.CLASS_NAME, 'spec_list').text
                product_size.append(f"{danawa_size1}")
            except:
                product_size.append(f"nonesize1")


    else:
        # Step1. 이마트몰의 첫번째 사진 클릭
        try:
            a = driver.find_element(By.CLASS_NAME, 'mnemitem_goods_tit').click()
        except:
            print(f"{i} : error")

        # 클릭된 이미지 이름 추출
        try:
            d = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[2]/div[2]/h2/span/span').text
            real_product_name.append(f"{i}_{d}")
            print()
        except:
            real_product_name.append(f"{i}_none4")

        # 이미지 추출
        try:
            b = driver.find_element(By.XPATH, '//*[@id="mainImg"]')
            # b.get_attribute('src')
            product_image.append(f"{i}_{b.get_attribute('src')}")
            print(f"{i} : img_success")
        except:
            product_image.append(f"{i}_none")
            print(f"{i} : not image")

        # 대분류 추출
        try:
            e = driver.find_element(By.XPATH, '//*[@id="location"]/div[2]/a').text
            big_cate.append(f"{i}_{e}")
        except:
            print() 
            
        # 중분류 추출
        try:
            g = driver.find_element(By.XPATH, '//*[@id="location"]/div[3]/a').text
            middle_cate.append(f"{i}_{g}")
        except:
            print()
            
        # 소분류 추출
        try:
            h = driver.find_element(By.XPATH, '//*[@id="location"]/div[4]/a').text
            small_cate.append(f"{i}_{h}")
        except:
            print()
            
        # 사이즈 추출
        try:
            c = driver.find_element(By.XPATH, '//*[@id="item_detail"]/div[1]/div[3]/div[2]/div/table/tbody/tr[4]/td/div').text
        except:
            print("")
            
        try:
            c2 = driver.find_element(By.XPATH, '//*[@id="item_detail"]/div[1]/div[3]/div[2]/div/table/tbody/tr[6]/td/div').text           
        except:
            print(f"{i} : not size3")

        product_size.append(f"{c}_{c2}")

        # Case2-1. 해당 상품이 있을 경우 (O) ->이마트몰에서 해당 상품 검색 -> 첫 번째 사진을 클릭 -> 아래 상세설명의 4번째 6번째 행 가져오기
        # Case2-2. 상세설명의 4번째 6번째 리스트가 "상세설명참조", "한국", "중국" 등 이면 다나와 검색 후 Case1-1, Case1-2 반복
        try:
            if c in ["상세설명 표기", "해당사항 없음", "상세설명참조", "상세페이지 참고", "상세정보설명참조", "한국", "중국"] or c2 == "상품상세참조":
                danawa_url = f"https://search.danawa.com/dsearch.php?query={i}"
                site = driver.get(danawa_url)
                time.sleep(random.uniform(5, 10))
                
                # [error1] - 2글자 이하로 검색시 나오는 문구
                try:
                    danawa_not_search1 = driver.find_element(By.ID, 'nosearchArea')
                except:
                    danawa_not_search1 = []
            
                # [error2] - 상품을 찾을 수 없을 때 나오는 문구
                try:
                    danawa_not_search2 = driver.find_element(By.XPATH, '//*[@id="nosearchArea"]/div/ul')
                except:
                    danawa_not_search2 = []
                
                if danawa_not_search1 or danawa_not_search2:
                    real_product_name.append(f"{i}_notsearch")
                    product_size.append("none_danawa")
                else:
                    danawa_click_name2 = driver.find_element(By.CLASS_NAME, 'prod_name').text
                    real_product_name[-1] = f"{i}_{danawa_click_name2}"
            
                    try:
                        danawa_size2 = driver.find_element(By.CLASS_NAME, 'spec_list').text
                        product_size[-1] = f"{danawa_size2}"
                    except:
                        product_size[-1] = f"{danawa_size2}"
        except:
            print("big problem")
