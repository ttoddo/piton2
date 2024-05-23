import requests
import webbrowser


status_code = input("Введите код статуса: ")
api_url = f'https://http.cat/{status_code}'
result = requests.get(f'https://http.cat/{status_code}')
if result.status_code == 200:
    res = f'https://http.cat/images/{status_code}.jpg'
    webbrowser.open(res)
else:
    print("не сработало :(")