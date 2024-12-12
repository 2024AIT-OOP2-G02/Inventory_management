from flask import Blueprint, render_template
from models import Order
from peewee import fn
from datetime import datetime

# Blueprintの作成
month_bp = Blueprint('month', __name__, url_prefix='/month')

def get_monthly_summary():
    # 月別の貸出数を集計するクエリ
    monthly_orders = (Order
        .select(
            fn.strftime('%Y-%m', Order.order_date).alias('month'),
            fn.COUNT(Order.id).alias('order_count')
        )
        .group_by(fn.strftime('%Y-%m', Order.order_date))
        .order_by(fn.strftime('%Y-%m', Order.order_date))
    )

    # 結果を辞書形式に変換
    month_data = [
        {
            'month': order.month, 
            'book_count': order.order_count
        } for order in monthly_orders
    ]

    return month_data