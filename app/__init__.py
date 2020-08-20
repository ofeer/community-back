from flask_restplus import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__)

from .main.controller.user_controller import api as user_ns
from .main.controller.carpool_controller import api as carpool_ns
api = Api(blueprint,
          title='Community',
          version='1.0',
          description=''
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(carpool_ns, path='/carpools')
