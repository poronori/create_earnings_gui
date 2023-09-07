from time import sleep
# chromeのドライバーを保持しておくためのクラス
class Driver:
    driver = None
    
    #ブラウザを監視する
    #バツで閉じたらdriverをNoneにする
    @staticmethod
    def polling():
        while Driver.driver != None:
            try:
                cur_url = Driver.driver.current_url
                sleep(1)
            except Exception:
                Driver.driver = None
        print("ドライバーオフ")