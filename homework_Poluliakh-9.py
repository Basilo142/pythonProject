# 1. *В якості тестового файла використовуйте python_zen.txt або будь-який інший файл з текстом англійскою
# Потрібно:
# - Вивести найпопулярніший символ цього фалу
# - Записати весь текст в новий файл задом на перед
# file_name = "python_zen.txt"
# with open(file_name) as file:
#      text = file.read()
#     # s = dict()
#     # for i in text:
#     #     s[i] = text.count(i)
#     # print(max(s.keys(), key=s.get))
#     # print("=" * 50)

# - Вивести речення з найбільшою кількістю пробілів
# file_name = "python_zen.txt"
# with open(file_name) as file:
#     text = file.read()
# sentences = text.split("\n")
# max_sent_spaces = sentences[0]
# for i in sentences:
#     if i.count(" ") > max_sent_spaces.count(" "):
#         max_sent_spaces = i
# print(max_sent_spaces)

#  - Записати весь текст в новий файл задом на перед
# file_name = "python_zen.txt"
# with open(file_name) as file:
#     for i in file:
#         out = i[::-1]
#         with open("out.txt", "a") as f:
#             f.write(out)

# 2. * В якості JSON файла викоритовуйте currecy.json.
# Потрібно:


#   - Вивиести повідомлення про кожну валюту в форматі "Курс ʼХʼ сьогодні ʼХʼ - на купівлю та ʼХʼ на продаж"
import json

currency = "currency.json"
with open(currency) as file:
    json_data = json.load(file)
    for dick_data in json_data:
        print(f"Курс {dick_data['ccy']} сьогодні {dick_data['buy']} - на купівлю та {dick_data['sale']} на продаж")

#  - Зберегти значення євро та доллара в новий файл

new_json_data = []
for val in json_data:
    if val['ccy'] in ('USD', 'EUR'):
        new_json_data.append(val)
with open("new_cu.json", 'w') as f:
    json.dump(new_json_data, f, indent=2)

#   - В оригінальний файл додати ще одну валюту (будь-яку на ваш розсуд та фантазію)

    json_data.append({'ccy': "GBP", 'bace_ccy': "UAH", 'buy': "47.000", 'sale': "44.000"})


with open(currency, 'w') as file:
    json.dump(json_data, file, indent=2, sort_keys=True)
