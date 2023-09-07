import flet as ft
from ..model.scraping import open,set_data
from .alert_view import AlertView
from .scraping_data_view import ScrapingDataList
from ..model.scraping_data import ScrapingData

def main(page):
    page.title = "取引管理ツール"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    alart = AlertView()
    dataList = ScrapingDataList()
    
    def add_click(e):
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
    
    capture_buttom = ft.ElevatedButton("データ取込", icon=ft.icons.ADD, on_click=add_click)
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        capture_buttom
                    ]
                ),
                dataList
            ]
        )
    )
    page.add(alart)
    page.dialog = alart