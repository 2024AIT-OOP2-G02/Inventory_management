from flask import Blueprint, render_template
from models import Product, Order
from peewee import fn

# Blueprintの作成
book_bp = Blueprint('book', __name__, url_prefix='/book')

def get_book_data():
    # 本の名前と貸出数を集計するクエリ
    book_data_query = (Product
        .select(
            Product.name.alias('name'),
            fn.COUNT(Order.id).alias('count')
        )
        .join(Order, on=(Order.product == Product.id))
        .group_by(Product.name)
        .order_by(Product.name)
    )

    # 結果を辞書形式に変換
    book_data = [
        {
            'name': product.name,
            'count': product.count
        } for product in book_data_query
    ]

    return book_data