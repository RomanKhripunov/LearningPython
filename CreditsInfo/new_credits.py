import json

import requests
from bs4 import BeautifulSoup as bs


HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
}

BASE_URL = 'https://myfin.by/kredity/zhile/?Kredity[city]=1&Kredity[amount]=80%20000&Kredity[review_period_h]=10000&Kredity[period]=180&Kredity[type_id]=6&Kredity[subtype_id]=&yt0=Подобрать'


def get_html(url):
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    if response.status_code == 200:
        print('OK')
    else:
        print('ERROR')
    return response.text


def main():
    soup = bs(get_html(BASE_URL), 'html.parser')
    table = soup.find('tbody', class_="table-body")

    for ind, div in enumerate(table.find_all('div', class_="product_bank_name_block"), start=1):
        print(ind, div.span.text, div.a.text)




if __name__ == '__main__':
    main()
