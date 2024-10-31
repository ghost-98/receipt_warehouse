# receipt 폴더 python 패키지로 인식하게 함 / 비어도 되고 모듈 초기화도 가능

from flask import Blueprint

receipt = Blueprint('receipt', __name__)

from . import routes  # 라우트 파일을 불러와서 블루프린트에 포함시킴
