import datetime

class ScrapingData :
    
    date = ''
    name = ''
    price = 0
    commission = 0
    customer = ''
    postcode = ''
    address1 = ''
    address2 = ''
    code = ''
    
    @staticmethod
    def set_scraping_data(date, name, price, commission, customer, postcode, address1, address2, code):
        ScrapingData.date = date
        ScrapingData.name = name
        ScrapingData.price = price
        ScrapingData.commission = commission
        ScrapingData.customer = customer
        ScrapingData.postcode = postcode
        ScrapingData.address1 = address1
        ScrapingData.address2 = address2
        ScrapingData.code = code
        
    @staticmethod
    def get_date():
        if not ScrapingData.date:
            return ''
        else:
            date = ScrapingData.date
            date_array = date.split(' ')
            return date_array[0][5:]
    
    @staticmethod
    def get_name():
        return ScrapingData.name
    
    @staticmethod
    def get_price():
        price = ScrapingData.price
        price = price.replace(',', '')
        return int(price)
    
    @staticmethod
    def get_commission():
        commission = ScrapingData.commission
        commission = commission.replace(',', '')
        return int(commission)
    
    # '様'を取り除く
    @staticmethod
    def get_customer():
        if not ScrapingData.customer:
            return ''
        else:
            customer = ScrapingData.customer
            return customer[0: len(customer) - 2]
    
    @staticmethod
    def get_customer_full():
        return ScrapingData.customer
    
    @staticmethod
    def get_postcode():
        return ScrapingData.postcode
    
    # '〇〇県'のみ取得
    @staticmethod
    def get_address():
        if not ScrapingData.address1:
            return ''
        else:
            address = ScrapingData.address1
            address_array = address.split(' ')
            return address_array[0]
    
    @staticmethod
    def get_address1():
        return ScrapingData.address1
    
    @staticmethod
    def get_address2():
        return ScrapingData.address2
    
    @staticmethod
    def get_code():
        return ScrapingData.code