from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from .scraping_data import ScrapingData
from .driver import Driver as dr
from ..view.scraping_data_view import ScrapingDataList
from ..view.alert_view import AlertView


def open(url) :
    print('===========Chromeを開く===========')
    userprofile = r"%USERINFO%\AppData\Local\Google\Chrome\User Data"
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + userprofile)
    options.add_argument('--profile-directory=Profile1') #アプリ用のプロファイルを使う
    dr.driver = webdriver.Chrome(options)
    dr.driver.get(url)

def get_data() :
    scraping = None
    cur_url = dr.driver.current_url
    print(cur_url)
    if "https://jp.mercari.com/" in cur_url:
        scraping = get_mercari_data()
    elif "https://www.yahoo.co.jp" in cur_url:
        scraping = get_paypay_data()
    else:
        AlertView.open("メルカリかペイペイフリマの取引画面を開いてください")
    
    return scraping

# メルカリのデータ取得
def get_mercari_data() :
    driver = dr.driver
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
    #shadowroot = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[2]/div/div[2]/a/mer-item-object').shadow_root
    #name = shadowroot.find_element(by=By.CLASS_NAME, value='item-label').text
    name = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div/div[2]/div/div[2]/a/div/div/div[2]/span').text #2024/1/13 エラーのため変更

    print(date)
    print(name)
    print(price)
    print(commission)
    print(customer)
    print(postcode)
    print(address)
    print(code)
    
    scraping = ScrapingData(
        date = date, 
        name = name, 
        price = price, 
        commission = commission, 
        customer = customer, 
        postcode = postcode, 
        address1 = address1, 
        address2 = address2, 
        code = code
    )
    return scraping

# ペイペイフリマのデータ取得
def get_paypay_data(driver) :
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
    return scraping