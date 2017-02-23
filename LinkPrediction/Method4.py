fin = open('friends1_NY.txt','rt')
line = len(fin.readlines())
fin.close()
user_order = []
user = 0

fin2 = open('Checkins_NY.txt','rt')
while True:
    check = fin2.readline()
    if not check:
        break
    a = check.split('\t')
    if a[0] not in user_order:
        user += 1
        user_order.append(a[0])

fin2.close()

fin_predict = open('friends1_NY.txt', 'rt')
#check_predict = []
relationship = []
for i in range(0,line):
    s1 = fin_predict.readline()
    a = s1.split("\t")
    new = []
    new.append(a[0])
    b = a[1].split("\n")
    new.append(b[0])
    relationship.append(new)
fin_predict.close()

for m in range(0,line):
    for n in range(0,line):
        if m != n and len(relationship[m]) != 0 and len(relationship[n]) != 0:
            if len(list(set(relationship[m]).intersection(set(relationship[n])))) >= 10:
                for k in range(0, len(relationship[n])):
                    if relationship[n][k] in relationship[m]:
                        relationship[n].remove(relationship[n][k])
                        relationship[m] += relationship[n]
                        relationship[n].clear()
                        break



for a in range(0,line):
    relationship[a] = list(set(relationship[a]))

name = 'friends4_NY.txt'
ff = open(name, 'w', encoding='UTF-8')
for i in range(0,line):
    if len(relationship[i]) != 0:
        for j in range(0, len(relationship[i])):
            for k in range(0, len(relationship[i])):
                if j != k:
                    ff.write("{0}\t{1}\n".format(relationship[i][j], relationship[i][k]))

ff.close()

fin_answer = open('friendship_NY.txt', 'rt')
check_answer = []
while 1:
    s1 = fin_answer.readline()
    check_answer.append(s1)
    if not s1:
        break
fin_answer.close()

fin_predict = open('friends4_NY.txt', 'rt')
check_predict = []
while 1:
    s2 = fin_predict.readline()
    check_predict.append(s2)
    if not s2:
        break
fin_predict.close()

tp = 0
for i in range(0, len(check_answer)):
    for j in range(0, len(check_predict)):
        if check_answer[i] == check_predict[j]:
            tp += 1

np = user * (user - 1) - len(check_answer) - len(check_predict) + tp
a = (tp + np) / (user * (user - 1))
p = tp / len(check_predict)
r = tp / len(check_answer)
f1 = (2 * p * r) / (p + r)
print("Accuracy: ",a,"\t","Precision: ",p,"\t","Recall: ",r,"\t","F1 score: ",f1)