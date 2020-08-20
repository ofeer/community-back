from flask import request, g, session, redirect, url_for
from flask_restplus import Resource
from flask_jwt import jwt_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, login

api = UserDto.api
user = UserDto.user
user_login = UserDto.user_login


@api.route('/register')
class UserRegister(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/login')
class UserLogin(Resource):
    @api.response(201, 'User successfully login.')
    @api.doc('login a user into the system')
    @api.expect(user_login, validate=True)
    def post(self):
        """login a user """
        data = request.json
        return login(data=data)


@api.route('/logout')
class Logout(Resource):
    @api.response(201, 'User successfully logout.')
    @api.doc('logout a user from the system')
    def get(self):
        """logout a user """
        return redirect(url_for('api.auth_user_login'))  # TODO: redirect to a page, should be changed in the end



