import requests


url_prb = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'


def pretty_view(data: list[dict]):

    result = [
        {
            f"{el.get('ccy')}": {
                'buy': float(el.get('buy')),
                'sale': float(el.get('sale')),
            }
        }
        for el in data
    ]
    pattern = '|{:<35}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in result:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


def pretty_view_nbu(data: list[dict], currency):
    result = {
            f"{el.get('cc')}": {
                'txt': el.get('txt'),
                'rate': float(el.get('rate')),
            }
        for el in data}
    pattern = '|{:<35}|{:^10}|{:^10}|'
    print(pattern.format('name', 'currency', 'rate'))
    print(pattern.format(result.get(currency).get('txt'), currency, result.get(currency).get('rate')))
    # for el in result:
    #     currency, *_ = el.keys()
    #     txt = el.get(currency).get('txt')
    #     rate = el.get(currency).get('rate')
    #     print(pattern.format(txt, currency, rate))


class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get(url)
        return response.json()


if __name__ == '__main__':
    client = ApiClient(requests)
    data = client.get_json(url_prb)
    pretty_view(data)
    data_nbu = client.get_json(url_nbu)
    pretty_view_nbu(data_nbu, 'USD')
