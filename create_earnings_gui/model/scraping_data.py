class ScrapingData :
    
    def __init__(self, date, name, price, commission, customer, postcode, address1, address2, code) :
        self.date = date
        self.name = name
        self.price = price
        self.commission = commission
        self.customer = customer
        self.postcode = postcode
        self.address1 = address1
        self.address2 = address2
        self.code = code
        
    def get_date(self):
        if not self.date:
            return ''
        else:
            date = self.date
            date_array = date.split(' ')
            return date_array[0][5:]
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        price = self.price
        price = price.replace(',', '')
        return int(price)
    
    def get_commission(self):
        commission = self.commission
        commission = commission.replace(',', '')
        return int(commission)
    
    # '様'を取り除く
    def get_customer(self):
        if not self.customer:
            return ''
        else:
            customer = self.customer
            return customer[0: len(customer) - 2]
    
    def get_customer_full(self):
        return self.customer
    
    def get_postcode(self):
        return self.postcode
    
    # '〇〇県'のみ取得
    def get_address(self):
        if not self.address1:
            return ''
        else:
            address = self.address1
            address_array = address.split(' ')
            return address_array[0]
    
    def get_address1(self):
        return ScrapingData.address1
    
    def get_address2(self):
        return ScrapingData.address2
    
    def get_code(self):
        return ScrapingData.code