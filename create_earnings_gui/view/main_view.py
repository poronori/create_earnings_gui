import flet as ft
from ..model.scraping import open,set_data
from .alert_view import AlertView

def main(page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 値を動的にしたい部分のControlインスタンスを作成
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    alart = AlertView()
    
    # マイナスボタンクリック時の処理
    def minus_click(e):
        #Controlインスタンスのvalueプロパティに代入
        txt_number.value = str(int(txt_number.value) - 1) 
        #ページを更新。(txt_number.update()としても良い。updateは子要素に伝達する)
        page.update() 

    # プラスボタンクリック時の処理
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
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