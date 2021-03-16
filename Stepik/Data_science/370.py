num_game = int(input())
output = {}
for _ in range(num_game):
    game = input().split(";")
    if game[0] not in output:
        output[game[0]] = [0, 0, 0, 0, 0]
    if game[2] not in output:
        output[game[2]] = [0, 0, 0, 0, 0]
    if int(game[1]) == int(game[3]):
        output[game[0]][2] += 1
        output[game[2]][2] += 1
    elif int(game[1]) > int(game[3]):
        output[game[0]][1] += 1
        output[game[2]][3] += 1
    else:
        output[game[0]][3] += 1
        output[game[2]][1] += 1

    output[game[0]][0] += 1
    output[game[2]][0] += 1
for key in output:
    output[key][4]=output[key][1]*3+output[key][2]
    print(str(key)+':',output[key][0],output[key][1],output[key][2],output[key][3],output[key][4])




# print(output)

