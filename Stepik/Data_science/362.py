mat = []
fiz = []
rus = []
sr_mat, sr_fiz, sr_rus = 0, 0, 0
with open('data.txt', 'w') as x:
    pass
with open('dataset_3363_4.txt') as f:
    for lin in f:
        st = lin.strip().split(';')
        mat.append(int(st[1]))
        fiz.append(int(st[2]))
        rus.append(int(st[3]))
        sr = (int(st[1])+int(st[2])+int(st[3]))/3
        with open('data.txt', 'a') as d:
            d.write(str(sr)+'\n')
for i in mat: sr_mat+=i
for i in fiz: sr_fiz+=i
for i in rus: sr_rus+=i
sr_mat = sr_mat/len(mat)
sr_fiz = sr_fiz/len(fiz)
sr_rus = sr_rus/len(rus)
with open('data.txt', 'a') as f:
    f.write(str(sr_mat)+' '+str(sr_fiz)+' '+str(sr_rus))
