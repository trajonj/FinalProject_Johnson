import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_read_query
import creds

app = flask.Flask(__name__) 
app.config["DEBUG"] = True 

masterPassword = 'password'
masterUsername = 'username'

@app.route('/api/login', methods=['GET'])
def login():
    if request.authorization and request.authorization.username == masterUsername and masterPassword == masterPassword:
            return "You are now logged in."
    return make_response('COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/api/airports', methods=['GET']) #route to get all records from the database
def api_airports_id():
    if 'id' in request.args:
        id = int(request.args['id']) #if the id exists then continue
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM airports"
    airports = execute_read_query(conn, sql)
    results = []

    for airport in airports:
        if airport['id'] == id:
            results.append(airports) #necessary if statement to check for rows in airports
    return jsonify(results)

@app.route('/api/airports', methods=['POST']) #route to add a record to the database
def add_airports():
    request_data = request.get_json() #requesting user input through json format
    newairportcode = request_data['airportcode']
    newairportname = request_data['airportname']
    newcountry = request_data['country']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "INSERT INTO airports (airportcode, airportname, country) VALUES ('%s', '%s', '%s')" % (newairportcode, newairportname, newcountry) #adding the user input into the column rows
    airports = execute_read_query(conn, sql)
    conn.commit()
    
    return "Add request successful"

@app.route('/api/airports', methods=['PUT']) #route to update an airport in the database by id
def update_airports():
    request_data = request.get_json()
    idtoUpdate = request_data['id'] #the parameter needed to find the record to update 
    updateairportcode = request_data['airportcode'] #defining which value will be updated
    updateairportname = request_data['airportname']
    updatecountry = request_data['country']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "UPDATE airports SET airportcode = '%s', airportname = '%s', country = '%s' WHERE (id = '%s')" % (updateairportcode, updateairportname, updatecountry, idtoUpdate) #sql query that gets sent to the database
    airports = execute_read_query(conn, sql)
    conn.commit()

    return "Update entry successful"

@app.route('/api/airports', methods=['DELETE']) #route to delete a record from the database by id
def delete_airports():
    request_data = request.get_json() #funtion to delete an airport record from the database
    idtoDelete = request_data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "DELETE FROM airports WHERE (id = '%s')" % (idtoDelete) #the delete query that will be passed to the database
    airports = execute_read_query(conn, sql)
    conn.commit()

    return "Delete request successful"

@app.route('/api/airports/all', methods=['GET'])
def api_airports_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM airports"
    airports = execute_read_query(conn, sql)
    return jsonify(airports)

#--------------------------------------------------------------

@app.route('/api/planes', methods=['GET']) #route to get all records from the database
def api_plane_id():
    if 'id' in request.args:
        id = int(request.args['id']) #if the id exists then continue
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM planes"
    planes = execute_read_query(conn, sql)
    results = []

    for plane in planes:
        if plane['id'] == id:
            results.append(planes) #necessary if statement to check for rows in planes
    return jsonify(results)
    
@app.route('/api/planes', methods=['POST']) #route to add a record to the database
def add_planes():
    request_data = request.get_json() #requesting user input through json format
    newplanemake = request_data['make']
    newplanemodel = request_data['model']
    newplaneayear = request_data['ayear']
    newplanecapacity = request_data['capacity']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "INSERT INTO planes (make, model, ayear, capacity) VALUES ('%s', '%s', '%s', '%s')" % (newplanemake, newplanemodel, newplaneayear, newplanecapacity) #adding the user input into the column rows
    planes = execute_read_query(conn, sql)
    conn.commit()
    
    return "Add request successful"

@app.route('/api/planes', methods=['PUT']) #route to update a plane in the database by id
def update_planes():
    request_data = request.get_json()
    idtoUpdate = request_data['id'] #the parameter needed to find the record to update 
    updateplanemake = request_data['make'] #defining which value will be updated
    updateplanemodel = request_data['model']
    updateayear = request_data['ayear']
    updatecapacity = request_data['capacity']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "UPDATE planes SET make = '%s', model = '%s', ayear = '%s', capacity = '%s' WHERE (id = '%s')" % (updateplanemake, updateplanemodel, updateayear, updatecapacity, idtoUpdate) #sql query that gets sent to the database
    planes = execute_read_query(conn, sql)
    conn.commit()

    return "Update entry successful"

@app.route('/api/planes', methods=['DELETE']) #route to delete a record from the database by id
def delete_planes():
    request_data = request.get_json() #funtion to delete a plane record from the database
    idtoDelete = request_data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "DELETE FROM planes WHERE (id = '%s')" % (idtoDelete) #the delete query that will be passed to the database
    planes = execute_read_query(conn, sql)
    conn.commit()

    return "Delete request successful"

@app.route('/api/planes/all', methods=['GET'])
def api_planes_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM planes"
    planes = execute_read_query(conn, sql)
    return jsonify(planes)

#--------------------------------------------------------------

@app.route('/api/flights', methods=['GET']) #route to get all records from the database
def api_flights_id():
    if 'id' in request.args:
        id = int(request.args['id']) #if the id exists then continue
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM flights"
    flights = execute_read_query(conn, sql)
    results = []

    for flight in flights:
        if flight['id'] == id:
            results.append(flights) #necessary if statement to check for rows in flights
    return jsonify(results)
    
@app.route('/api/flights', methods=['POST']) #route to add a record to the database
def add_flights():
    request_data = request.get_json() #requesting user input through json format
    newplaneid = request_data['planeid']
    newairportfromid = request_data['airportfromid']
    newairporttoid = request_data['airporttoid']
    newadate = request_data['adate']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "INSERT INTO flights (planeid, airportfromid, airporttoid, adate) VALUES ('%s', '%s', '%s', '%s')" % (newplaneid, newairportfromid, newairporttoid, newadate) #adding the user input into the column rows
    flights = execute_read_query(conn, sql)
    conn.commit()
    
    return "Add request successful"

@app.route('/api/flights', methods=['DELETE']) #route to delete a record from the database by id
def delete_flights():
    request_data = request.get_json() #funtion to delete a flight record from the database
    idtoDelete = request_data['id']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "DELETE FROM flights WHERE (id = '%s')" % (idtoDelete) #the delete query that will be passed to the database
    flights = execute_read_query(conn, sql)
    conn.commit()

    return "Delete request successful"

@app.route('/api/flight/all', methods=['GET'])
def api_flights_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM flight"
    flights = execute_read_query(conn, sql)
    return jsonify(flights)




app.run()