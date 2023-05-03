import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Worker, Model, Vehicle, Unit, Reservation

# from sqlalchemy.dialects.postgresql  import insert, select
from sqlalchemy import insert, update, select

Base = sqlalchemy.orm.declarative_base()

engine = create_engine('postgresql+psycopg2://cadu:@localhost/desk', echo=True)


def insert_worker(name, document_number):
    stmt = insert(Worker).values(name=name, document_number=document_number)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def insert_model(car_manufacturer, model):
    stmt = insert(Model).values(car_manufacturer=car_manufacturer, model=model)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def insert_vehicle(color, licence_plate, model_id, worker_id):
    stmt = insert(Vehicle).values(color=color, licence_plate=licence_plate, model_id=model_id, worker_id=worker_id)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def insert_unit(name, total_work_desks, total_parking_spaces):
    stmt = insert(Unit).values(name=name, total_work_desks=total_work_desks, total_parking_spaces=total_parking_spaces)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()



def convertBooleanToInteger(boolean_value):
    if boolean_value:
        return 1
    else:
        return 0


def insert_reservation(date, worker_id, unit_id, vehicle_id, is_included_desk, is_included_parking):

    stmt = insert(Reservation).values(
                                            date=date,
                                            worker_id=worker_id,
                                            unit_id=unit_id,
                                            vehicle_id=vehicle_id,
                                            is_included_desk=convertBooleanToInteger(is_included_desk),
                                            is_included_parking=convertBooleanToInteger(is_included_parking))
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()


def update_reservation(reservation_id, unit_id, vehicle_id, is_included_desk, is_included_parking):

    stmt = update(Reservation).where(Reservation.id == reservation_id).values(unit_id=unit_id,
                                                                              vehicle_id=vehicle_id,
                                                                              is_included_desk=convertBooleanToInteger(is_included_desk),
                                                                              is_included_parking=convertBooleanToInteger(is_included_parking))
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()




update_reservation(reservation_id=5, unit_id=1, vehicle_id=3, is_included_desk=0, is_included_parking=0)
