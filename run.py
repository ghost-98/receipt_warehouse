# run.py가 전체를 실행하게 만들어줌
# app.__init__에서 if __name__=='__main__' 구조로 실행시킬수 있으나 관례가 아님. 초기화하는 파일이므로 따로 run.py같은 실행파일 생성

from app import create_app  # __init__.py에 있는 함수 이렇게 import가능

# app.__init__의 앱 객체
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드에서 실행
