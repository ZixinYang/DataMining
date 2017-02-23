from datetime import datetime
import math

fin = open('Checkins_PA.txt','rt')
line = len(fin.readlines())
fin.close()
fin2 = open('Checkins_PA.txt','rt')
who = []
time = []
visit = []
date_object = []
user = 0
user_order = []
loc_order = []
# 一行一行讀取資料，存進who、time、visit的陣列裡
while True:
    check = fin2.readline()
    if not check:
        break
    a = check.split('\t')
    who.append(a[0])
    if a[0] not in user_order:
        user += 1
        user_order.append(a[0])
    if a[4].split('\n')[0] not in loc_order:
        loc_order.append(a[4].split('\n')[0])
    time.append(a[1])
    visit.append(a[4].split('\n')[0])
fin2.close()

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
for k in range(0,line):
    date_object.append(datetime.strptime(time[k],DATETIME_FORMAT))

visit_frequency = []
visit_who = []
for i in range(len(loc_order)):
    visit_frequency.append(0)
    new = []
    for j in range(len(visit)):
        if loc_order[i] == visit[j]:
            visit_frequency[i]+=1
            new.append(who[j])
    visit_who.append(new)

locdiv = []
temp = ''
for i in range(len(visit_who)):
    a = []
    for j in range(len(visit_who[i])):
        if j == 0:
            temp = visit_who[i][j]
            a.append(1)
        else:
            if temp != visit_who[i][j]:
                temp == visit_who[i][j]
                a.append(1)
            else:
                a[len(a)-1] += 1
    calculate = 0
    for k in range(len(a)):
        calculate += (-1)*(a[k]/visit_frequency[i])*math.log(a[k]/visit_frequency[i])
    new = []
    new.append(loc_order[i])
    new.append(math.exp(calculate))
    locdiv.append(new)

locdiv.sort(key=lambda x:x[1], reverse=True)

popular_site = []
for i in range(25):
    popular_site.append(locdiv[i][0])


name = 'popular_site_PA.txt'
ff = open(name, 'w', encoding='UTF-8')
for i in range(len(popular_site)):
    ff.write("{0}\n".format(popular_site[i]))
ff.close()

name = 'friends5_PA.txt'
ff = open(name, 'w', encoding='UTF-8')

who_who =[]
for i in range(0, line):
    for j in range(0, line):
        # 同年同月同日，一個小時前後，同個地點，不是同一個人
        if i != j \
                and date_object[i].year == date_object[j].year \
                and date_object[i].month == date_object[j].month \
                and date_object[i].day == date_object[j].day \
                and visit[i] == visit[j] \
                and visit[i] not in popular_site \
                and who[i] != who[j]:
            if who[i]+'\t'+who[j] not in who_who:
                who_who.append(who[i]+'\t'+who[j])
                ff.write("{0}\t{1}\n".format(who[i],who[j]))
ff.close()

fin_answer = open('friendship_PA.txt', 'rt')
check_answer = []
while 1:
    s1 = fin_answer.readline()
    check_answer.append(s1)
    if not s1:
        break
fin_answer.close()

fin_predict = open('friends5_PA.txt', 'rt')
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