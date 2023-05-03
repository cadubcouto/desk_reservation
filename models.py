import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship


Base = sqlalchemy.orm.declarative_base()

engine = create_engine('postgresql+psycopg2://cadu:@localhost/desk', echo=True)

class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    document_number = Column(String)

    def __repr__(self):
        return f'Worker {self.name}'


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, primary_key=True)
    car_manufacturer = Column(String)
    model = Column(String)

    def __repr__(self):
        return f'Model {self.car_manufacturer}-{self.model}'


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    color = Column(String)
    licence_plate = Column(String)
    model_id = Column(Integer, ForeignKey('model.id'))
    Model = relationship('Model')
    worker_id = Column(Integer, ForeignKey('worker.id'))
    Worker = relationship('Worker')


    def __repr__(self):
        return f'Vehicle {self.Model}-{self.color}-{self.licence_plate}'


class Unit(Base):
    __tablename__ = 'unit'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    total_work_desks = Column(Integer)
    total_parking_spaces = Column(Integer)

    def __repr__(self):
        return f'Unit {self.name}'


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    worker_id = Column(Integer, ForeignKey('worker.id'))
    Worker = relationship('Worker')
    unit_id = Column(Integer, ForeignKey('unit.id'))
    Unit = relationship('Unit')
    is_included_desk = Column(Integer)
    is_included_parking = Column(Integer)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    Vehicle = relationship('Vehicle')


    def __repr__(self):
        return f'Reserva {self.Unit}-{self.date}'


Base.metadata.create_all(engine)

