from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import messagebox
from .scraping_data import ScrapingData

def open() :
    print('===========取引情報取得　開始===========')
    result = True
    # 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options)
    
    cur_url = driver.current_url
    print(cur_url)
    if "https://jp.mercari.com/" in cur_url:
        set_mercari_data(driver)
    elif "https://www.yahoo.co.jp" in cur_url:
        set_paypay_data(driver)
    else :
        messagebox.showwarning('URL不正', f'メルカリかペイペイフリマの取引画面を開いてください。{cur_url}')
        result = False
    
    print('===========取引情報取得　終了===========')
    return result

# メルカリのデータ取得
def set_mercari_data(driver) :
    
    date = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[3]/div[5]/div[2]/span').text
    price = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[3]/div[1]/div[2]/span/span/span[2]').text
    commission = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[3]/div[2]/div[2]/span/span/span[2]').text
    code = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[3]/div[6]/div[2]/span/div/p').text
    postcode = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[4]/div/div[2]/span/div/p[1]').text
    address1 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[4]/div/div[2]/span/div/p[2]').text
    address2 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[4]/div/div[2]/span/div/p[3]').text

    #建物名がない場合はaddress2に購入者名が入る
    try:
        customer = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[4]/div/div[2]/span/div/p[4]').text
    except Exception:
        customer = address2
        address2 = ''
    address = address1 + ' ' + address2
    
    #商品名はsharow-root内にあるので、別途取得する
    shadowroot = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[2]/div/div[2]/a/mer-item-object').shadow_root
    name = shadowroot.find_element(by=By.CLASS_NAME, value='item-label').text
    
    print(date)
    print(name)
    print(price)
    print(commission)
    print(customer)
    print(postcode)
    print(address)
    print(code)
    
    scraping = ScrapingData()
    scraping.set_scraping_data(
        date = date, 
        name = name, 
        price = price, 
        commission = commission, 
        customer = customer, 
        postcode = postcode, 
        address1 = address1, 
        address2 = address2, 
        code = code)

# ペイペイフリマのデータ取得
def set_paypay_data(driver) :
    date = '2023年9月1日 12:05'
    name = 'ペイペイの品名'
    price = '2,000'
    commission = '100'
    customer = 'サンプル 花子'
    postcode = '〒123-3456'
    address = '東京都 なんとか区 ほげほげ'
    code = 'b123456789'
    
    scraping = ScrapingData()
    scraping.set_scraping_data(
        date = date, 
        name = name, 
        price = price, 
        commission = commission, 
        customer = customer, 
        postcode = postcode, 
        address = address, 
        code = code)