# /usr/bin/python3.9
import requests
import lxml
from bs4 import BeautifulSoup


def get_vaccination():
    url = "https://www.mohfw.gov.in/"
    req = requests.request(method='GET', url=url)

    soup = BeautifulSoup(req.text, 'lxml')
    time = soup.find('section', {'id': 'site-dashboard', 'class': 'site-stats'})
    lst = time.div.div.find_all('div', {'class': 'col-xs-12'})
    res = []
    res.extend(lst)
    req = res[1].text
    req = req.strip()
    return ''.join(req.split('\n'))


if __name__ == '__main__':
    r = get_vaccination()

    print(r)
