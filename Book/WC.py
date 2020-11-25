import sys
import requests
url = sys.argv[1]
try:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
except requests.Timeout:
    print('Превышен таймаут,', url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("Ochibka", code)
except requests.RequestException:
    print("Ошибка скачивания")
else:
    print(resp.content)