from flask import request, jsonify
from flask_restplus import Resource
from ..util.dto import CarpoolDto
from ..service.carpool_service import save_new_ride, list_of_rides, get_all_rides
from app.main.model.carpool import Carpool
from flask_cors import cross_origin

api = CarpoolDto.api
carpool = CarpoolDto.carpool
carpool_search = CarpoolDto.carpool_search


@api.route('/newDrive')
class AddDrive(Resource):
    @cross_origin()
    @api.response(201, 'drive successfully created.')
    @api.doc('create a new drive')
    @api.expect(carpool, validate=True)
    def post(self):
        """Creates a new drive """
        data = request.json

        return save_new_ride(data=data)


@api.route('/findDrive')
class GetDrives(Resource):
    @api.doc('gets requested drives')
    @api.expect(carpool_search, validate=True)
    def post(self):
        """gets requested drives"""
        data = request.json
        return list_of_rides(data=data)


@api.route('/allDrives')
class GetAllDrives(Resource):
    @api.doc('gets all active drives')
    def post(self):
        """gets all active drives"""
        return get_all_rides()


def get_all_drives():
    return Carpool.query.first()
