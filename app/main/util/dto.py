from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        #  TODO: add student card
    })

    user_login = api.model('user_login', {

        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),

    })


# TODO: change all to fields to date / time and so on
class CarpoolDto:
    api = Namespace('carpool', description='carpool')
    carpool = api.model('carpool', {
        'when': fields.String(required=True, description='carpool date'),
        'start': fields.String(required=True, description=''),
        'destination': fields.String(required=True),
        'hour': fields.String(required=True),
        'number_of_sits': fields.Integer(required=True),
        'animal': fields.Boolean(default=False),
        'road6': fields.Boolean(default=False),
        'comments': fields.String(required=False, description='driver comments for the ride')
    })
    carpool_search = api.model('carpool_search', {
        'when': fields.String(required=True, description='carpool date'),
        'start': fields.String(required=True, description=''),
        'destination': fields.String(required=True),
        'hour': fields.String(required=True),
    })
