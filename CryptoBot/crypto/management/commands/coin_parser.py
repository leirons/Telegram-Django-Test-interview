import requests
import bs4


def get_coins(name):
    """Собирает информацию о трех монетах, которые находятся в списке coins"""
    headers = 'Your headers'  # Не обязательно.
    _URL = 'https://minfin.com.ua/currency/crypto/'
    r = requests.get(_URL)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    coins = ['Bitcoin', 'Ethereum', 'Dogecoin']  # может быть улучшено.
    result = []  # хранит основные результаты

    for i in coins:
        crypto = soup.find('div',title=f'{i}')
        values = crypto.parent
        crypto_value = values.find('span',class_='coin-price--num').text
        crypto_name = crypto.find('span',class_='blue coin-name--long').text
        result.append(
            {
                'crypto_name':crypto_name,
                'crypto_value':crypto_value[:-3],
            }
        )
    for i in result:
        if name in i.values():
            return i











