import json
import logging
from flask import Flask, request, redirect, Response
from flask_cors import CORS, cross_origin
from db import insert_worker, insert_model, insert_vehicle, insert_unit, insert_reservation, update_reservation
from db_select import select_reservations, select_worker, select_reservations_by_document_number, \
    select_reservationByDateAndWork, select_vehicle_by_worker_id, select_reservations_by_worker_id


app = Flask(__name__)
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG



@app.route('/api/v1/worker', methods=['POST'])
def create_worker():
    name = request.args.get('name')
    document_number = request.args.get('document_number')
    insert_worker(name=name, document_number=document_number)
    output = {'msg': 'Worker criado com sucesso'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    return response


@app.route('/api/v1/model', methods=['POST'])
def create_model():
    car_manufacturer = request.args.get('car_manufacturer')
    model = request.args.get('model')
    insert_model(car_manufacturer=car_manufacturer, model=model)
    output = {'msg': 'Modelo criado com sucesso'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    return response


@app.route('/api/v1/vehicle', methods=['POST'])
def create_vehicle():
    color = request.args.get('color')
    licence_plate = request.args.get('licence_plate')
    model_id = request.args.get('model_id')
    worker_id = request.args.get('worker_id')
    insert_vehicle(color=color, licence_plate=licence_plate, model_id=model_id, worker_id=worker_id)
    output = {'msg': 'Veiculo criado com sucesso'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    return response


@app.route('/api/v1/unit', methods=['POST'])
def create_unit():
    name = request.args.get('name')
    total_work_desks = request.args.get('total_work_desks')
    total_parking_spaces = request.args.get('total_parking_spaces')
    insert_unit(name=name, total_work_desks=total_work_desks, total_parking_spaces=total_parking_spaces)
    output = {'msg': 'Estacionamento criado com sucesso'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    return response


@app.route('/api/v1/reservation', methods=['POST'])
def create_reservation():
    content = request.json
    print(content)
    print(content['worker_id'])
    date = content['date']
    worker_id = content['worker_id']
    unit_id = content['unit_id']
    is_included_desk = content['is_included_desk']
    is_included_parking = content['is_included_parking']
    vehicle_id = None
    vehicles = select_vehicle_by_worker_id(worker_id=worker_id)
    if len(vehicles) > 0: vehicle_id = vehicles[0]['id']
    reservations = select_reservationByDateAndWork(date=date, worker_id=worker_id)
    if len(reservations) > 0:
        update_reservation(reservation_id=reservations[0]['id'],
                           unit_id=unit_id,
                           vehicle_id=vehicle_id,
                           is_included_parking=is_included_parking,
                           is_included_desk=is_included_desk)
    else:
        insert_reservation( date =  date,
                            worker_id = worker_id,
                            unit_id = unit_id,
                            vehicle_id = vehicle_id,
                            is_included_desk = is_included_desk,
                            is_included_parking = is_included_parking)

    output = {  'sucess' : True,
                'msg': 'Reserva Criada ou alterada com Sucesso'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/v1/reservation/reservation_by_date', methods=['GET'])
def get_reservations():
    output = select_reservations(request.args.get('date'))
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=200
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/v1/reservation/reservation_by_document_number', methods=['GET'])
def get_reservation_of_worker_by_document_id():
    output = select_reservations_by_document_number(request.args.get('document_number'))
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=200
    )
    return response


@app.route('/api/v1/desk/reservation_by_worker_id', methods=['GET'])
def get_reservation_of_worker_by_worker_id():
    output = select_reservations_by_worker_id(request.args.get('worker_id'))
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=200
    )
    return response


@app.route('/api/v1/worker', methods=['GET'])
def get_worker():
    document_number = request.args.get('document_number')
    output = select_worker(document_number=document_number)
    print(output)
    if len(output) > 0:
        response = json.dumps(output[0]),
    else:
        response = "{}"
    response = Response(
        mimetype="application/json",
        response=response,
        status=200
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)

