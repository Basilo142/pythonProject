import requests

with open('dataset_3378_2.txt') as x:
    for lin in x:
        url=lin.strip()
new = requests.get(url).text.splitlines()
print(len(new))

