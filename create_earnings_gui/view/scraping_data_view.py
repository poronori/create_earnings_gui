import flet as ft
from ..model.scraping_data import ScrapingData

# データリストのビュー
class ScrapingDataList(ft.UserControl):
    
    def __init__(self):
        super().__init__(self)
        self.dataList = []
        self.dataListView = ft.Column()
    
    def add_data(self, data):
        dataView = ScrapingDataView(data, self.data_delete)
        self.dataListView.controls.append(dataView)
        self.dataListView.update()
    
    def build(self):
        return self.dataListView
    
    def data_delete(self, data):
        self.dataListView.controls.remove(data)
        self.update()

#個別のデータビュー
class ScrapingDataView(ft.UserControl):
    
    def __init__(self, data:ScrapingData, data_delete):
        super().__init__(self)
        self.date = ft.Text(f'購入日：{data.get_date()}')
        self.name = ft.Text(f'品名：{data.get_name()}')
        self.price = ft.Text(f'商品代金：{data.get_price()}')
        self.commission = ft.Text(f'販売手数料：{data.get_commission()}')
        self.customer = ft.Text(f'購入者：{data.get_customer()}')
        self.postcode = ft.Text(f'郵便番号：{data.get_postcode()}')
        self.address1 = ft.Text(f'住所１；{data.get_address1()}')
        self.address2 = ft.Text(f'住所２：{data.get_address2()}')
        self.code = ft.Text(f'コード：{data.get_code()}')
        
        self.data_delete = data_delete
        
    def delete_click(self, e):
        self.data_delete(self)
    
    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    [
                        self.date,
                        self.name,
                        self.price,
                        self.commission,
                        self.customer,
                        self.postcode,
                        self.address1,
                        self.address2,
                        self.code
                    ]
                ),
                ft.IconButton(
                    ft.icons.DELETE_OUTLINE,
                    tooltip="Delete Data",
                    on_click=self.delete_click,
                ),
            ]
        )
