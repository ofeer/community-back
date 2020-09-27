import uuid
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()  # checks if the email exist already
    if not user:
        new_user = User(
            user_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object
    else:
        response_object = {
            'status': 'fail',
            'message': 'email already exists. Please Log in.',
        }
        return response_object


def login(data):
    username = data['username']
    password = data['password']
    user = get_a_user_by_name(username)
    if user:
        if User.check_password(user, password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            response_object = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'status': 'success',
                'message': 'Successfully logged in.'
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'passwords does not match.',
                'username': data['username'],
                'password': data['password']
            }
            return response_object
    else:
        response_object = {
            'status': 'fail',
            'message': 'username does not match.',
            'username': data['username'],
            'password': data['password']
        }
        return response_object


def get_all_users():
    return User.query.all()


def get_a_user_by_name(username):
    return User.query.filter_by(username=username).first()


def get_a_user_by_id(user_id):
    return User.query.filter_by(user_id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
