import requests
with open('dataset_3378_3.txt') as x:
    for lin in x:
        url=lin.strip()
print(url)
new = requests.get(url).text
print(type(new), new)

while "We" not in new:
    new = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+new).text
    print(new)

print("Molodec!!!!!!!!!")