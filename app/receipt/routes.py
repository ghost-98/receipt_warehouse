# http 요청 처리하는 파일. 경로 설정과 뷰 함수 동시에 정의 (views+urls)

from flask import Blueprint, request, jsonify  # request와 jsonify?
from werkzeug.utils import secure_filename  # flask 내장
from .models import Receipt
from .. import db

receipt = Blueprint('receipt', __name__)

@receipt.route('/upload', methods=['POST'])  # app.__init__에 receipt가 url_prefix로 매핑되어있음
def upload_receipt():
    # 파일 업로드 및 OCR 처리 로직
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # 파일 처리 및 OCR 수행
    filename = secure_filename(file.filename)
    filepath = f'app/uploads/{filename}'
    file.save(filepath)

    # 예시 텍스트 데이터 및 파싱
    text_data = "Sample text from OCR"
    new_receipt = Receipt(
        store_name="Sample Store",
        date="2024-10-31",
        total_amount="15.50",
        text_data=text_data,
        image_path=filepath
    )
    db.session.add(new_receipt)
    db.session.commit()

    # 파일 저장 및 데이터베이스 처리 (예시)
    return jsonify({'message': 'Receipt uploaded successfully'}), 201
