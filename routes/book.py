from models import Product
from models import Order
from models.db import db
from peewee import *

def get_book_data():
    book_name = [] # 本の名前を入れておく配列
    
    for product in Product.select():
        book_name.append(product.name) # 名前の取得
    
    book_count = [0] * len(book_name)
    
    # 書名ごとにカウントする
    for i, name in enumerate(book_name):
        print(name, i)
        query = Order.select().where(Order.product == (i + 1))
        for book in query:
            book_count[i] += 1
            
    # print(book_count)

    return [book_name,book_count]