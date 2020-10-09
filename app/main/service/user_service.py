import uuid
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()  # checks if the email exist already
    if not user:
        if len(data['password']) > 5:
            new_user = User(
                id=str(uuid.uuid4()),
                email=data['email'],
                firstName=data['firstName'],
                lastName=data['lastName'],
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
                'message': 'Password to short',
            }
            return response_object
    else:
        response_object = {
            'status': 'fail',
            'message': 'email already exists. Please Log in.',
        }
        return response_object


def login(data):
    email = data['email']
    password = data['password']
    user = get_a_user_by_email(email)
    if user:
        if User.check_password(user, password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            response_object = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'status': 'success',
                'email': data['email'],
                'firstName': user.firstName,
                'lastName': user.lastName
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'passwords does not match.',
                'email': data['email'],
                'password': data['password']
            }
            return response_object
    else:
        response_object = {
            'status': 'fail',
            'message': 'username does not match.',
            'email': data['email'],
            'password': data['password']
        }
        return response_object


def get_all_users():
    return User.query.all()


def get_a_user_by_email(email):
    return User.query.filter_by(email=email).first()


def get_a_user_by_id(user_id):
    return User.query.filter_by(user_id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
