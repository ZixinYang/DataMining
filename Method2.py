from datetime import datetime
import calendar

# 判斷兩個時間，是否相差在一個小時以內
def dateDiffInHours(date1, date2):
    if date1 - date2 == 1 or date1 - date2 == 0 or date1 - date2 == -1:
        return True
    else:
        return False


def isWeekdayMorning(year,month,day,hour):
    if calendar.weekday(year, month, day) == 5 or calendar.weekday(year, month, day) == 6:
        return False
    else:
        if hour < 16 or hour > 3:
            return True
        else:
            return False

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
    time.append(a[1])
    visit.append(a[4])
fin2.close()

# 二維陣列宣告，用來儲存兩兩之間在同一個地點且接近的時間打卡的次數
count = []
for i in range(0,user):
    new = []
    for j in range(0,user):
        new.append(0)
    count.append(new)


# 將時間字串轉成datetime
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
for k in range(0,line):
    date_object.append(datetime.strptime(time[k],DATETIME_FORMAT))

frequency = []
for i in range(0,user):
    frequency.append(0)

for i in range(0, line):
    w = user_order.index(who[i])
    frequency[w] += 1
    for j in range(0, line):
        # 同年同月同日，一個小時前後，同個地點，不是同一個人
        if date_object[i].year == date_object[j].year \
                and date_object[i].month == date_object[j].month \
                and date_object[i].day == date_object[j].day \
                and dateDiffInHours(date_object[i].hour, date_object[j].hour) \
                and visit[i] == visit[j] \
                and who[i] != who[j] \
                and isWeekdayMorning(date_object[i].year,date_object[i].month,date_object[i].day,date_object[i].hour) \
                and isWeekdayMorning(date_object[j].year,date_object[j].month,date_object[j].day,date_object[j].hour):
            index1 = user_order.index(who[i])  # 計算此id是第幾個人
            index2 = user_order.index(who[j])
            count[index1][index2] += 1  # 兩人接近時間同地打卡的頻率加1


sim = []
for i in range(0,user):
    sim_u = []
    for j in range(0,user):
        sim_u.append(float((count[i][j])/(frequency[i]+frequency[j]-count[i][j])))
    sim.append(sim_u)
threshold = 0
for i in range(0,user):
    for j in range(0,user):
        threshold += sim[i][j]

threshold /= (user*(user-1))

print(threshold)

name = 'friends2_new_PA.txt'
ff = open(name, 'w', encoding='UTF-8')
for i in range(0,user):
    for j in range(0,user):
        if sim[i][j] > threshold:
            ff.write("{0}\t{1}\n".format(user_order[i],user_order[j]))
ff.close()

fin_answer = open('friendship_PA.txt', 'rt')
check_answer = []
while 1:
    s1 = fin_answer.readline()
    check_answer.append(s1)
    if not s1:
        break
fin_answer.close()

fin_predict = open('friends2_new_PA.txt', 'rt')
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