from flask import request, jsonify, session

from . import user
from .models import User
from .. import db

@user.route('/register', methods=['POST'])
def register():
    data = request.json  # 요청에서 json데이터 파싱, dic
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': '이미 존재하는 아이디입니다'}), 400

    # 새 유저 생성 후 db에 저장
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()  # db에 변경사항 커밋

    return jsonify({'message': '회원가입이 성공적으로 완료되었습니다'}), 201

@user.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        session['user_id'] = user.id  # 사용자의 세션에 데이터 저장
        return jsonify({'message': '로그인 성공'}), 200

    return jsonify({'error': '유효하지 않은 아이디나 비밀번호입니다'}), 401

@user.route('/logout', methods=['POST'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')  # 사용자 세션 제거
        return jsonify({'message': '로그아웃 완료'}),200
    else:  # 이런 예외가 있나?
        return jsonify({'error': '로그인 되어있지 않은 사용자입니다'}), 400
