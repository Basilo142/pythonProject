def line_up(hints):
    left = 'left'
    right = 'right'
    list_result = []
    line = hints.pop(0)
    if line.split()[5] == left:
        list_result.append(line.split()[2])
        list_result.append(line.split()[0])
    else:
        list_result.append(line.split()[0])
        list_result.append(line.split()[2])

    hints = [[i.split()[0], i.split()[2], i.split()[5]] for i in hints]
    while hints:
        print('l-', list_result)
        s = hints.pop(0)
        print('s-', s)
        if s[0] in list_result and s[1] in list_result:
            pass
        elif s[0] not in list_result and s[1] not in list_result:
            hints.append(s)

        else:
            if s[0] in list_result:
                list_result.insert(0, s[1]) if s[2] == 'left' else list_result.append(s[1])
            else:
                list_result.insert(0, s[0]) if s[2] == right else list_result.append(s[0])

    return list_result


hints1 = [
    "white has black on his left",
    "red has green on his right",
    "black has green on his left"
]
h2 = ["green has pink on his left",
                                    "green has white on his right",
                                    "black has red on his right",
                                    "red has blue on his right",
                                    "black has white on his left"]

h3 = ["red has green on his right", "green has red on his left"]
h3_result = ['red', 'green']

if __name__ == '__main__':
    print(line_up(h3))
