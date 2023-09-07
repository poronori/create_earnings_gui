import flet as ft
from ..model.scraping import open,get_data
from ..model.edit_excel import edit
from ..model.driver import Driver as dr
from .alert_view import AlertView
from .scraping_data_view import ScrapingDataList
from ..model.scraping_data import ScrapingData

def main(page):
    page.title = "取引管理ツール"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    # データがなくなったらボタンを押せなくする
    def delete():
        write_button.disabled = True
        page.update()
        
    alart = AlertView()
    dataList = ScrapingDataList(delete)
    
    def add_click(e):
        scraping = get_data()
        '''
        scraping = ScrapingData(
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
        '''
        if scraping != None:
            dataList.add_data(scraping)
            write_button.disabled = False
            page.update()
    
    #メルカリを開く
    def mercari_click(e):
        #ブラウザが開いている間のボタン制御
        mercari_button.disabled = True
        capture_button.disabled = False
        page.update()
        try:
            open("https://jp.mercari.com/")
            # ブラウザの監視
            dr.polling()
            # ブラウザが閉じた時のボタン制御
            mercari_button.disabled = False
            capture_button.disabled = True
            page.update()
        except Exception:
            #変な風に閉じるとエラーが発生するので、その時のボタン制御
            mercari_button.disabled = False
            capture_button.disabled = True
            page.update()
    
    def write_click(e):
        edit(dataList)
    
    capture_button = ft.ElevatedButton("データ取込", icon=ft.icons.ADD, on_click=add_click, disabled = True)
    mercari_button = ft.ElevatedButton("メルカリを開く", on_click=mercari_click)
    write_button = ft.ElevatedButton("エクセルに書き込む", icon=ft.icons.NOTE_ADD, on_click=write_click, disabled=True)
    
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        mercari_button,
                        capture_button,
                        write_button
                    ]
                ),
                dataList
            ]
        )
    )
    page.add(alart)
    page.dialog = alart