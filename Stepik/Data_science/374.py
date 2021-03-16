for i in range(11):
    class_line = []
    with open('dataset_3380_5.txt') as f:

        for l in f:
            lin = l.split()
            if int(lin[0]) == i+1:
                class_line.append(int(lin[2]))
        if len(class_line) !=0:
            print(i+1, sum(class_line)/len(class_line))
        else:
            print(i+1, '-')

