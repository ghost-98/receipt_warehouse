# Flask 앱 설정 및 초기화

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 인스턴스 생성
db = SQLAlchemy()

# 이 구조가 뭘까?
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 권장 설정

    # SQLAlchemy 인스턴스와 앱 연결
    db.init_app(app)

    from .routes import main
    from .receipt import receipt  # 순환 db참조 방지위해 여기서 import

    # 블루프린트 등록
    app.register_blueprint(main)
    app.register_blueprint(receipt, url_prefix='/receipt')

    return app  # 플라스크 애플리케이션 객체 반환
