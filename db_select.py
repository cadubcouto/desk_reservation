from db_postgre import DBPG as DB

DATABASE_IP_APP="localhost"
USER_DATABASE_APP="cadu"

db_desk = DB(   IP=DATABASE_IP_APP,
                user=USER_DATABASE_APP,
                password=None,
                db='desk')


def select_reservations(date):
    sql = f"SELECT u.id, u.name, SUM(is_included_desk) as total_desk_reservation, SUM(is_included_parking) as total_parking_reservation, u.total_work_desks, u.total_parking_spaces " \
          f"FROM public.reservation as r " \
          f"RIGHT JOIN public.unit as u " \
          f"ON r.unit_id = u.id AND Date(r.date) = '{date}' " \
          f"GROUP BY u.id ORDER BY u.name"

    print(sql)
    return db_desk.select(sql=sql)


def select_reservationByDateAndWork(date, worker_id):
    sql = f"SELECT * F" \
          f"ROM public.reservation " \
          f"WHERE date = '{date}' and worker_id = '{worker_id}' " \
          f"LIMIT 1";
    print(sql)
    return db_desk.select(sql=sql)



def select_worker(document_number):
    sql = f"SELECT * " \
          f"FROM public.worker as w " \
          f"WHERE w.document_number = '{document_number}'"
    print(sql)
    return db_desk.select(sql=sql)


def select_reservations_by_document_number(document_number):
    sql = f"SELECT CAST(date AS TEXT) as date_reservation, u.name, r.is_included_desk, r.is_included_parking, m.car_manufacturer, m.model, v.color, v.licence_plate FROM reservation as r " \
          f"LEFT JOIN unit as u ON r.unit_id = u.id " \
          f"LEFT JOIN worker as w On r.worker_id = w.id " \
          f"LEFT JOIN vehicle as v On r.vehicle_id = v.id " \
          f"LEFT JOIN model as m On v.model_id = m.id where document_number = '{document_number}'"
    print(sql)
    return db_desk.select(sql=sql)


def select_reservations_by_worker_id(worker_id):
    sql = f"SELECT CAST(date AS TEXT) as date_reservation, u.name, r.is_included_desk, r.is_included_parking, m.car_manufacturer, m.model, v.color, v.licence_plate FROM reservation as r " \
          f"LEFT JOIN unit as u ON r.unit_id = u.id " \
          f"LEFT JOIN worker as w On r.worker_id = w.id " \
          f"LEFT JOIN vehicle as v On r.vehicle_id = v.id " \
          f"LEFT JOIN model as m On v.model_id = m.id where r.worker_id = '{worker_id}'"
    print(sql)
    return db_desk.select(sql=sql)


def select_vehicle_by_worker_id(worker_id):
    sql = f"SELECT * " \
          f"FROM public.vehicle " \
          f"WHERE worker_id = '{worker_id}' " \
          f"LIMIT 1"
    print(sql)
    return db_desk.select(sql=sql)



print(select_reservations_by_worker_id(3))

