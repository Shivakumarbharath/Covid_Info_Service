# usr/bin/python3.9
import requests
import lxml
from bs4 import BeautifulSoup


def get_tests():
    url = "https://www.icmr.gov.in/"
    r = requests.request(method='GET', url=url)
    sp = BeautifulSoup(r.text, 'lxml')
    k = sp.find_all('div', {'class': 'col-12'})[2].text.strip().split('\n\n\n\n\n\n\n')
    l = []
    for e in k:
        if e != '':
            l.append('\n'.join(e.split('\n')[::-1]))
    return '\n\n'.join(l)


if __name__ == '__main__':
    print(get_tests())
