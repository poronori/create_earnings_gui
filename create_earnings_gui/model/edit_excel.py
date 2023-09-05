import openpyxl
import configparser
import datetime
from copy import copy
from .scraping_data import ScrapingData

def edit() : 
    print('===========エクセルに記入 開始===========')
    
    #設定ファイルからエクセルのパスを取得
    inifile = configparser.SafeConfigParser()
    inifile.read('config/config.ini', encoding='utf-8')
    excel_path = inifile.get('DEFAULT', 'ExcelPath')
    print(excel_path)
    wb = openpyxl.load_workbook(excel_path)
    
    #販売リスト
    add_create_list(wb)
    #宛名
    ws = wb['宛名']
    edit_addressee(ws)
    ws = wb['宛名 圧迫厳禁']
    edit_addressee(ws)

    wb.save(excel_path)
    
    print('===========エクセルに記入 終了===========')

# 販売リストに追記
def add_create_list(wb):
    
    date = ScrapingData.get_date()
    name = ScrapingData.get_name()
    price = ScrapingData.get_price()
    commission = ScrapingData.get_commission()
    customer = ScrapingData.get_customer()
    address = ScrapingData.get_address()
    code = ScrapingData.get_code()
    current_year = datetime.date.today().year
    
    print('購入日：   ' + date)
    print('品名：     ' + name)
    print('商品代金：  ' + str(price))
    print('販売手数料：' + str(commission))
    print('購入者：    ' + customer)
    print('配送先；    ' + address)
    print('コード：    ' + code)
    
    ws = wb['販売リスト %s' %current_year]
    
    #一番下の行を取得
    maxRow = ws.max_row
    #max_rowを使うと削除していた行も取得してしまうため、Noneで判定する
    for row in ws.iter_rows():
        if not row[0] or row[0].value is None :
            maxRow = row[0].row - 1
            break
    print('追加行:' + str(maxRow))
    nextRow = maxRow + 1
    
    #行を挿入
    ws.insert_rows(nextRow)
    
    #書式をコピー
    i = 1
    profit = ''
    for row in ws.iter_rows():
        for cell in row:
            if cell.row == maxRow:
                ws.cell(row = nextRow, column = i).border = copy(cell.border)
                ws.cell(row = nextRow, column = i)._style = copy(cell._style)
                value = cell.value
                #計算式をコピー
                if str(value)[0] == "=":
                    profit = value.replace(str(maxRow), str(nextRow))
                i = i + 1

    #値をセット
    no = ws.cell(row = maxRow, column = 1).value
    ws.cell(row = nextRow, column = 1).value = int(no) + 1   #No
    ws.cell(row = nextRow, column = 2).value = date          #購入日
    ws.cell(row = nextRow, column = 3).value = name          #品名
    ws.cell(row = nextRow, column = 4).value = price         #商品代金
    ws.cell(row = nextRow, column = 5).value = commission    #販売手数料
    ws.cell(row = nextRow, column = 6).value = ''            #梱包資材１   
    ws.cell(row = nextRow, column = 7).value = '封筒'        #梱包資材２
    ws.cell(row = nextRow, column = 8).value = ''            #送料
    ws.cell(row = nextRow, column = 9).value = profit        #販売利益
    ws.cell(row = nextRow, column = 10).value = customer     #購入者
    ws.cell(row = nextRow, column = 11).value = address      #住所
    ws.cell(row = nextRow, column = 12).value = code         #コード

def edit_addressee(ws):
    postcode = ScrapingData.postcode
    address1 = ScrapingData.get_address1()
    address2 = ScrapingData.get_address2()
    customer = ScrapingData.get_customer_full()
    
    ws['B2'].value = postcode
    ws['B3'].value = address1
    ws['B4'].value = address2
    ws['B6'].value = customer

#日時を〇月×日にフォーマット
def string_to_datetime(date_string) :
    datetime_array = date_string.split('/')
    year = int(datetime_array[0])
    month = int(datetime_array[1])
    day = int(datetime_array[2])
    dt = datetime.date(year, month, day)
    
    return dt.strftime('%m月%d日')

#住所から県名を抽出
def prefecture_from_address(address) :
    index = address.find('県', 0, 4)
    if index != -1 :
        return address[0:index + 1]
    
    index = address.find('府', 0, 3)
    if index != -1 :
        return address[0:index + 1]
    
    if '北海道' in address :
        return address[0:3]
    
    if '東京都' in address :
        return address[0:3]