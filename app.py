from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.gender import Gender

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    gender_data = {
        "gender_count": [Gender().Count(0), Gender().Count(1)]
    }
    return render_template('index.html', gender_data=gender_data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
