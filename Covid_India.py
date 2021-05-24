#/usr/bin/python3
import requests
import json

headers = {
    'x-rapidapi-key': "4b72f0fea9msh22e1f9fa79fdb6cp1b15edjsn624eb33a7745",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
}
global total_values, state, state_meta, dist_meta, dist


def get_number_data():
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
	global total_values, state, state_meta, dist_meta, dist
	response = requests.request("GET", url, headers=headers)
	main_data = json.loads(response.text)
	total_values = main_data['total_values']
	total_values.pop('statecode')
	total_values.pop('state')
	state = main_data['state_wise']
	state_meta = ['state', 'active', 'confirmed', 'deaths', 'deltaconfirmed', 'deltadeaths',
                  'deltarecovered', 'lastupdatedtime', 'recovered',
                  'statecode', 'statenotes']
	dist = lambda x, y: x[y]
	dist_meta = ['notes', 'active', 'confirmed', 'deceased', 'recovered', 'delta']


get_number_data()


def get_state(state_param):
	s_dict = {}
	try:
		for e in state_meta:
			s_dict[e] = state[state_param][e]
#		print(state.keys())
		return s_dict
	except KeyError:
		return "Error"


def get_district(state_param, dist_param):
	try:
		return dist(dist(dist(state, state_param), 'district'), dist_param)
	except KeyError:
		return "Error"
def dist_error(state_param,dist_param):
	return dist(dist(state,state_param),'district')

def total():
	return total_values


if __name__ == '__main__':
	print(total(), type(total()))
	print(get_state('Maharashtra'), type(get_state('Maharashtra')))
	print(get_district('Karnataka', 'Yadgir'),"Yadgir")
