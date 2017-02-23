from datetime import datetime
import math, os

def dis(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

f1 = open('friends1_NY.txt', 'rt')
check = []
while 1:
    s1 = f1.readline()
    if not s1:
        break
    check.append(s1.split('\n')[0])
f1.close()
f2 = open('friends2_NY.txt', 'rt')
while 1:
    s2 = f2.readline()
    if not s2:
        break
    check.append(s2.split('\n')[0])
f2.close()

f3 = open('average_min_dis_NY.txt', 'rt')
while 1:
    s3 = f3.readline()
    if not s3:
        break
    check.append(s3.split('\n')[0])
f3.close()

f4 = open('friends4_NY.txt', 'rt')
while 1:
    s4 = f4.readline()
    if not s4:
        break
    check.append(s4.split('\n')[0])
f4.close()
f5 = open('friends5_NY.txt', 'rt')
while 1:
    s5 = f5.readline()
    if not s5:
        break
    check.append(s5.split('\n')[0])
f5.close()

check = list(set(check))

#print(check)

fin = open('Checkins_NY.txt','rt')
line = len(fin.readlines())
fin.close()
fin2 = open('Checkins_NY.txt','rt')
who = []
time = []
visit = []
date_object = []
user = 0
user_order = []
loc_order = []
long_lat = []
# 一行一行讀取資料，存進who、time、visit的陣列裡
while True:
    check1 = fin2.readline()
    if not check1:
        break
    a = check1.split('\t')
    who.append(a[0])
    if a[0] not in user_order:
        user += 1
        user_order.append(a[0])
    if a[4].split('\n')[0] not in loc_order or a[2]+'\t'+a[3] not in long_lat:
        loc_order.append(a[4].split('\n')[0])
        long_lat.append(a[2] + '\t' + a[3])
    time.append(a[1])
    visit.append(a[4].split('\n')[0])

fin2.close()

print('length of User:',user)
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

who_visit = []
for i in range(len(user_order)):
    new = []
    for j in range(len(who)):
        if who[j]!=user_order[i]:
            continue
        elif who[j]==user_order[i]:
            new.append(visit[j])
            temp = user_order[i]
        elif temp!=who[j]:
            break
    who_visit.append(list(set(new)))

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
print(len(locdiv))
ldpd = []
loc_list = []
who_list = []
for i in range(len(check)):
        new = []
        if check[i].split('\t')[1]+'\t'+check[i].split('\t')[0] not in who_list:
            who_list.append(check[i])
            d = []
            l = []
            for k1 in range(len(who_visit[user_order.index(check[i].split('\t')[0])])):
                for k2 in range(len(who_visit[user_order.index(check[i].split('\t')[1])])):
                    if k1 != k2 and who_visit[user_order.index(check[i].split('\t')[1])][k2]+'\t'+who_visit[user_order.index(check[i].split('\t')[0])][k1] not in loc_list:
                            loc_list.append(who_visit[user_order.index(check[i].split('\t')[0])][k1]+'\t'+who_visit[user_order.index(check[i].split('\t')[1])][k2])
                            d.append(dis(float(long_lat[loc_order.index(who_visit[user_order.index(check[i].split('\t')[0])][k1])].split('\t')[0]), float(long_lat[loc_order.index(who_visit[user_order.index(check[i].split('\t')[0])][k1])].split('\t')[1]), float(long_lat[loc_order.index(who_visit[user_order.index(check[i].split('\t')[1])][k2])].split('\t')[0]), float(long_lat[loc_order.index(who_visit[user_order.index(check[i].split('\t')[1])][k2])].split('\t')[1])))
                            l.append(max(locdiv[loc_order.index(who_visit[user_order.index(check[i].split('\t')[0])][k1])][1],locdiv[loc_order.index(who_visit[user_order.index(check[i].split('\t')[1])][k2])][1]))
                            #print('Max of locdiv:',max(locdiv[k1][1],locdiv[k2][1]))
                            new.append(d[len(d)-1]*l[len(l)-1])
            if len(new)!=0:
                w = []
                w.append(int(check[i].split('\t')[0]))
                w.append(int(check[i].split('\t')[1]))
                w.append(min(new))
                ldpd.append(w)
ldpd.sort(key=lambda x:x[2], reverse=False)
print('lenghth of ldpd:', len(ldpd))

name = 'friends3_NY.txt'
ff = open(name, 'w', encoding='UTF-8')
for i in range(len(ldpd)):
    ff.write("{0}\t{1}\n".format(str(ldpd[i][0]),str(ldpd[i][1])))
    ff.write("{0}\t{1}\n".format(str(ldpd[i][1]), str(ldpd[i][0])))
    if i == 8000:
        break
ff.close()