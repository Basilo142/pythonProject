import json
import pprint
import requests
from bs4 import BeautifulSoup
from decimal import Decimal
'''
Австралійський долар - 'AUD'
Канадський долар - 'CAD'
Юань Женьміньбі - 'CNY'
Куна - 'HRK'
Чеська крона - 'CZK'
Данська крона - 'DKK'
Гонконгівський долар - 'HKD'
Форинт - 'HUF'
Індійська рупія - 'INR'
Рупія - 'IDR'
Новий ізраїльський шекель - 'ILS'
Єна - 'JPY'
Теньге - 'KZT'
Вона - 'KRW'
Мексиканське песо - 'MXN'
Молдовський лей - 'MDL'
Новозеландський долар - 'NZD'
Норвезька крона - 'NOK'
Російський рубль - 'RUB'
Саудівський ріял - 'SAR'
Сінгапурський долар - 'SGD'
Ренд - 'ZAR'
Шведська крона - 'SEK'
Швейцарський франк - 'CHF'
Єгипетський фунт - 'EGP'
Фунт стерлінгів - 'GBP'
Долар США - 'USD'
Білоруський рубль - 'BYN'
Румунський лей - 'RON'
Турецька ліра - 'TRY'
СПЗ (спеціальні права запозичення) - 'XDR'
Болгарський лев - 'BGN'
Євро - 'EUR'
Злотий - 'PLN'
Алжирський динар - 'DZD'
Така - 'BDT'
Вірменський драм - 'AMD'
Іранський ріал - IRR
Іракський динар - IQD
Сом - KGS
Ліванський фунт - LBP
Лівійський динар - LYD
Малайзійський ринггіт - MYR
Марокканський дирхам - MAD
Пакистанська рупія - PKR
Донг - VND
Бат - THB
Дирхам ОАЕ - AED
Туніський динар - TND
Узбецький сум - UZS
Туркменський новий манат - TMT
Сербський динар - RSD
Азербайджанський манат - AZN
Сомоні - TJS
Ларі - GEL
Бразильський реал - BRL
Золото - XAU
Срібло - XAG
Платина - XPT
Паладій - XPD
'''


def curs_usa_eur(vals):
    result = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    a = result.json()

    cur = []
    cur_out = []
    for val in vals:
        cur.append([i for i in a if i['cc'] == val][0])
    for i in cur:
        cur_out.append('Курс-{} на {} - {}'.format(i['txt'].ljust(35), i['exchangedate'], i['rate']))
    return cur_out


if __name__ == '__main__':
    ex = curs_usa_eur(['USD', 'EUR'])
    pprint.pprint(ex)