name, score, combination = [], [], []
for i in range(int(input('how many students ? '))):
    name.append(input('enter a name: '))
    score.append(float(input('enter a score: ')))
minno = min(score)
names2 = name.copy()
scores2 = score.copy()
for i in range(len(score)):
    if score[i] == minno:
        names2.remove(name[i])
        scores2.remove(score[i])
for i in range(len(names2)):
    comb = names2[i], scores2[i]
    combination.append(comb)
minno2 = min(scores2)
names3=[]
for i in range(len(names2)):
    if scores2[i] == minno2:
        names3.append(names2[i])
names3.sort()
for i in range(len(names3)):
    print(names3[i])