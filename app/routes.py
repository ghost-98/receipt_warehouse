from flask import Blueprint, render_template

# 블루프린트 설정
main = Blueprint('main', __name__)

@main.route('/')
def first_page():
    return render_template('first_page.html')  # flask 기본제공 렌더링 함수 - templates 폴더가 기본 경로인가?

