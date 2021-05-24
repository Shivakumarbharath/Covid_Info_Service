# usr/bin/lib/python3.9
import functools
from cowin.api import CoWinAPI
import json

h = CoWinAPI()


def find_state(state, list):
    for e in list:
        if e['state_name'] == state:
            return e['state_id']
def error_dist(state):
    #try:

    state_id=find_state(state,h.get_states()['states'])
    districts=h.get_districts(str(state_id))
    if len(districts['districts'])<1:
        return "Error"
    else:
        return districts
    #except:
     #   return "Error"
def find_district(dist, state):
    state_id = find_state(state, h.get_states()['states'])
    districts = h.get_districts(str(state_id))
    for e in districts['districts']:
        if e['district_name'] == dist:
            return e['district_id']


def get_sessions(dist, state):

    if not dist == "Bangalore":
        id = find_district(dist, state)
        # print('WEEK',h.get_availability_by_district_week(district_id=str(id)))
        return h.get_availability_by_district_week(str(id))
    else:
        l = ["Bangalore Rural", "Bangalore Urban", 'BBMP']
        send = []
        for e in l:
            id = find_district(e, state)
            # print('WEEK', h.get_availability_by_district_week(district_id=str(id)))
            send += h.get_availability_by_district_week(str(id))['centers']
            return {'centers':send}


if __name__ == '__main__':
    state = input("State ?").capitalize()
    dist = input("District?").capitalize()
    y = get_sessions(dist, state)
    print(len(json.dumps(y)))
    print(type(y))
   # print(error_dist("Karnataka"))
   # print(error_dist('kdj'))
