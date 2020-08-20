from flask import request
from flask_restplus import Resource
from ..util.dto import CarpoolDto
from ..service.carpool_service import save_new_ride, list_of_rides
from app.main.model.carpool import Carpool

api = CarpoolDto.api
carpool = CarpoolDto.carpool
carpool_search = CarpoolDto.carpool_search


@api.route('/new drive')
class AddDrive(Resource):
    @api.response(201, 'drive successfully created.')
    @api.doc('create a new drive')
    @api.expect(carpool, validate=True)
    def post(self):
        """Creates a new drive """
        data = request.json
        return save_new_ride(data=data)


@api.route('/find drive')
class GetDrives(Resource):
    @api.doc('gets all active drives')
    @api.expect(carpool_search, validate=True)
    def post(self):
        """gets all active drives"""
        data = request.json
        return list_of_rides(data=data)


def get_all_drives():
    return Carpool.query.first()
