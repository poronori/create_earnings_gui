import flet as ft
from ..model.scraping import open,set_data
from .alert_view import AlertView
from .scraping_data_view import ScrapingDataList
from ..model.scraping_data import ScrapingData

def main(page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 値を動的にしたい部分のControlインスタンスを作成
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    alart = AlertView()
    dataList = ScrapingDataList()
    
    # マイナスボタンクリック時の処理
    def minus_click(e):
        #Controlインスタンスのvalueプロパティに代入
        txt_number.value = str(int(txt_number.value) - 1) 
        #ページを更新。(txt_number.update()としても良い。updateは子要素に伝達する)
        page.update() 

    # プラスボタンクリック時の処理
    def plus_click(e):
        data = ScrapingData(
            date = '2023年9月1日 12:05',
            name = 'ペイペイの品名',
            price = '2,000',
            commission = '100',
            customer = 'サンプル 花子',
            postcode = '〒123-3456',
            address1 = '東京都 なんとか区 ほげほげ',
            address2 = '鴻池ビル 14階',
            code = 'b123456789'
        )
        dataList.add_data(data)
        page.update()
        
    def cabin_click(e):
        open("https://wwww.yahoo.co.jp")
    
    def game_click(e):
        set_data()
    
    def add_click(e):
        set_data()
        
    page.add(
        ft.Column(
            [
                dataList,
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                        txt_number,
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ],
                ),
                ft.IconButton(ft.icons.CABIN, on_click=cabin_click),
                ft.IconButton(ft.icons.GAMEPAD, on_click=game_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(alart)
    page.dialog = alart