import requests


def main():
    cities = ('Лондон', 'Шереметьево', 'Череповец')
    params = {
            'mnTq': '',
            # m - метрическая система, n - узкая версия, T - без цвета,
            # q - без текста "Прогноз погоды" (подробно: http://wttr.in/:help)
            'lang': 'ru'
            }
    url_template = 'http://wttr.in/{}'
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params)
        if response.ok:
            print(response.text)


if __name__ == '__main__':
    main()
