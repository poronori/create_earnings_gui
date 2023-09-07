import flet as ft
from ..model.scraping_data import ScrapingData

# データリストのビュー
class ScrapingDataList(ft.UserControl):
    
    def __init__(self):
        super().__init__(self)
        self.dataList = []
        self.dataListView = ft.Column()
    
    def add_data(self, data):
        dataView = ScrapingDataView(data)
        self.dataListView.controls.append(dataView)
        self.dataListView.update()
    
    def build(self):
        return self.dataListView

#個別のデータビュー
class ScrapingDataView(ft.UserControl):
    
    def __init__(self, data:ScrapingData):
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
    
    def build(self):
        return ft.Column(
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
        )
    
