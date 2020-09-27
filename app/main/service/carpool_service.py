from flask import jsonify
import json
from app.main import db
from app.main.model.carpool import Carpool
from flask_jwt_extended import get_jwt_identity, jwt_required


# @jwt_required
def save_new_ride(data):
    #  TODO: add a check that a user upload one drive only (per 6 hours?)
    new_ride = Carpool(
        driver_id=get_jwt_identity(),
        when=data['when'],
        start=data['start'],
        destination=data['destination'],
        hour=data['hour'],
        number_of_sits=data['number_of_sits'],
        animal=data['animal'],
        road6=data['road6'],
        comments=data['comments']
    )
    save_changes(new_ride)
    response_object = {
        'status': 'success',
        'message': 'Successfully created a ride.'
    }
    return response_object


def to_json(listofrides):
    rides = []
    for ride in listofrides:
        rides.append({'start': f'{ride.start}', 'destination': f'{ride.destination}', 'hour': f'{ride.hour}'})
    return rides


# @jwt_required
def list_of_rides(data):
    rides = Carpool.query.filter_by(when=data['when'], start=data['start'],
                                    destination=data['destination']).order_by('hour').all()
    if len(rides) == 0:
        response_object = {
            'status': 'success',
            'message': 'No rides in this date.'
        }
    else:
        response_object = {
            'status': 'success',
            'rides': to_json(rides)
        }
    return response_object


def save_changes(data):
    db.session.add(data)
    db.session.commit()
