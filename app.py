import json

from flask import Flask, request
import requests

app = Flask(__name__)
japan_airline_realtime = "https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightInformationDeparture?odpt:operator=odpt.Operator:JAL&acl:consumerKey=";
access_token = "d630af844f6fe79780ccb0b7144af4b2cd497d752d82d034c2002d559f564593";


@app.route('/api/v1/resources/flight', methods=["GET"])
def api_params():
    param = {}
    if 'flight_num' in request.args:
        flight_num = request.args['flight_num']
        param.put("flight_num", flight_num)
    if 'destination' in request.args:
        destination = request.args['destination']
        param.put("destination", destination)
    if 'departure' in request.args:
        departure = request.args['departure']
        param.put("departure", departure)
    if (len(param) == 0):
        return "Error: Please specify at least one parameter"
    elif ('departure' in param.keys() and 'destination' not in param.keys()):
        return "Error: Please specify the destination!"
    elif ('destination' in param.keys() and 'departure' not in param.keys()):
        return "Error: Please specify the departure airport!"
    # fetch from API for the flight details
    message = requests.get(japan_airline_realtime + access_token);
    if (message.status_code == requests.codes.ok):
        message = message.text;
        flights = json.loads(message);

        flights_clean = []
        for flight in flights:
            del flight['@context']
            del flight['owl:sameAs']
            del flight['@id']
            del flight['dc:date']
            del flight['dct:valid']
            # if flight has already left, remove it from flights
            if not 'odpt:actualDepartureTime' in flight.keys():
                flights_clean.append(flight);


    else:
        print(message.status_code);








if __name__ == '__main__':
    app.run()
