import requests;
import json;

access_token = "d630af844f6fe79780ccb0b7144af4b2cd497d752d82d034c2002d559f564593";
all_flights_arrival = "https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightInformationDeparture?odpt:operator=odpt.Operator:HND-JAT&acl:consumerKey=";
all_flights_departure = "https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightInformationDeparture?odpt:operator=odpt.Operator:HND-JAT&acl:consumerKey=";
japan_airline = "https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightSchedule?odpt:operator=odpt.Operator:JAL&acl:consumerKey="
japan_airline_realtime = "https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightInformationDeparture?odpt:operator=odpt.Operator:JAL&acl:consumerKey=";

# message = requests.get(japan_airline_realtime+access_token);
# if (message.status_code == requests.codes.ok):
#     message = message.text;
#     flights = json.loads(message);
#
#     flights_clean = []
#     for flight in flights:
#         del flight['@context']
#         del flight['owl:sameAs']
#         del flight['@id']
#         del flight['dc:date']
#         del flight['dct:valid']
#         # if flight has already left, remove it from flights
#         if not 'odpt:actualDepartureTime' in flight.keys():
#             flights_clean.append(flight);
#     print (flights_clean)
#
# else:
#     print (message.status_code);

message = requests.get("https://api-tokyochallenge.odpt.org/api/v4/odpt:FlightSchedule?odpt:operator=odpt.Operator:HND-JAT&acl:consumerKey=d630af844f6fe79780ccb0b7144af4b2cd497d752d82d034c2002d559f564593")
flight = json.loads(message.text)[0]
print (flight)