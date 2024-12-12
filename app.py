from flask import Flask, render_template
from models import initialize_database
from routes import blueprints

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    book_data = get_book_data()
    gender_data = get_gender_data()
    month_data = get_month_data()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
