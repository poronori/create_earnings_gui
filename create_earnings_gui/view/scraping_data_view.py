import flet as ft
from ..model.scraping_data import ScrapingData

class ScrapingDataList():
    
    def __init__(self):
        super().__init__(self)
        self.dataList = []
    
    def add_data(self, data):
        self.dataList.append(data)

class ScrapingDataView(ft.UserControl):
    
    def __init__(self, data:ScrapingData):
        super().__init__(self)
        self.date = data.get_date()
        self.name = data.get_name()
        self.price = data.get_price()
        self.commission = data.get_commission()
        self.customer = data.get_customer()
        self.postcode = data.get_postcode()
        self.address1 = data.get_address1()
        self.address2 = data.get_address2()
        self.code = data.get_code()
