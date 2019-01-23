import json

import requests
from bs4 import BeautifulSoup


CREDITS_URL = 'https://finance.tut.by/credits/nedvizhimost'


def get_html(url):
    response = requests.get(url)
    return response.text


def page_has_credits(page_text):
    return '{credits_block}' not in page_text


def get_all_uniq_urls(html):
    soup = BeautifulSoup(html, 'lxml')
    soup_banks = soup.find('table', class_='banks-table').find_all('tr', itemtype="http://schema.org/LoanOrCredit")
    return list(set([bank.get('data-href') for bank in soup_banks]))


def get_bank_data(html):
    soup = BeautifulSoup(html, 'lxml')

    header = soup.find('div', class_='cc-header__title').find('a')
    bank = header.text
    site = header.get('href')

    terms_table = soup.find('dl', class_='definitions-list')
    terms_params = terms_table.find_all('span', text=True)
    terms_values = terms_table.find_all('dd', text=True)
    terms = {k.text: v.text for k, v in zip(terms_params, terms_values)}

    calculations = soup.find('div', {'data-place': 'calculation'})
    calc_params = calculations.find('thead').find_all('th')
    calc_offers = calculations.find('tbody').find_all('tr')

    offers = {}
    for ind, offer in enumerate(calc_offers):
        offers[ind] = {k.text: v.text for k, v in zip(calc_params, offer.find_all('td'))}

    data = {
        'bank': bank,
        'site': site,
        'offers': (offers, {'terms': terms})
    }
    return data


def write_to_json(data):
    with open('credits.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print('\n\033[1;36mJSON file created successfully.\033[0m')


def get_offers(url):
    print('Get data by URL:', url, end='', flush=True)

    html = get_html(url)
    data = get_bank_data(html)

    print(' ' * 8, '\033[0;32m[DONE]\033[0m')
    return data


def main():
    banks_urls = get_all_uniq_urls(get_html(CREDITS_URL))

    all_banks_credits = [get_offers(bank_url) for bank_url in banks_urls]

    write_to_json(all_banks_credits)


if __name__ == '__main__':
    main()
