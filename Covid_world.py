import requests
import json

headers = {
    'x-rapidapi-key': "4b72f0fea9msh22e1f9fa79fdb6cp1b15edjsn624eb33a7745",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
}


def get_country(country):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    try:
        response = requests.request("GET", url, headers=headers)
        world = json.loads(response.text)['countries_stat']
        c_lists = list(map(lambda x: x['country_name'], world))
        return world[c_lists.index(country)]
    except ValueError:
        return "Error"


if __name__ == '__main__':
    print(get_country(input("Country Name").capitalize()))
