def vote(a,b,c):
    for i in range(len(c)):
        aa = c[i].split('\t')
        if aa[0]==a and aa[1].split('\n')[0]==b:
            return True
    return False

f1 = open('friends1_NY.txt', 'rt')
check1 = []
while 1:
    s1 = f1.readline()
    if not s1:
        break
    check1.append(s1)
f1.close()
f2 = open('friends2_NY.txt', 'rt')
check2 = []
while 1:
    s2 = f2.readline()
    if not s2:
        break
    check2.append(s2)
f2.close()
f3 = open('friends3_NY.txt', 'rt')
check3 = []
while 1:
    s3 = f3.readline()
    if not s3:
        break
    check3.append(s3)
f3.close()
f4 = open('friends4_NY.txt', 'rt')
check4 = []
while 1:
    s4 = f4.readline()
    if not s4:
        break
    check4.append(s4)
f4.close()
f5 = open('friends5_NY.txt', 'rt')
check5 = []
while 1:
    s5 = f5.readline()
    if not s5:
        break
    check5.append(s5)
f5.close()

user = 0
user_order = []
f = open('friendship_NY.txt','rt')
while 1:
    s = f.readline()
    a = s.split('\t')
    if not s:
        break
    if a[0] not in user_order:
        user_order.append(a[0])
        user += 1
f.close()
name = 'friends_combo.txt'
ff = open(name, 'w', encoding='UTF-8')


user_list = []
for i in range(len(check1)):
    count = 0
    if check1[i] not in user_list:
        if check1[i] in check2:
            count += 1
        if check1[i] in check3:
            count += 1
        if check1[i] in check4:
            count += 1
        if check1[i] in check5:
            count += 1
        if count >= 2:
            user_list.append(check1[i].split('\n')[0])
            user_list.append(check1[i].split('\t')[1].split('\n')[0] + '\t' + check1[i].split('\t')[0])
for i in range(len(check2)):
    count=0
    if check2[i] not in user_list:
        if check2[i] in check1:
            count += 1
        if check2[i] in check3:
            count += 1
        if check2[i] in check4:
            count += 1
        if check2[i] in check5:
            count += 1
        if count >= 2:
            user_list.append(check2[i].split('\n')[0])
            user_list.append(check2[i].split('\t')[1].split('\n')[0] + '\t' + check2[i].split('\t')[0])
for i in range(len(check3)):
    count=0
    if check3[i] not in user_list:
        if check3[i] in check1:
            count += 1
        if check3[i] in check2:
            count += 1
        if check3[i] in check4:
            count += 1
        if check3[i] in check5:
            count += 1
        if count >= 2:
            user_list.append(check3[i].split('\n')[0])
            user_list.append(check3[i].split('\t')[1].split('\n')[0] + '\t' + check3[i].split('\t')[0])
for i in range(len(check4)):
    count=0
    if check4[i] not in user_list:
        if check4[i] in check1:
            count += 1
        if check4[i] in check2:
            count += 1
        if check4[i] in check3:
            count += 1
        if check4[i] in check5:
            count += 1
        if count >= 2:
            user_list.append(check4[i].split('\n')[0])
            user_list.append(check4[i].split('\t')[1].split('\n')[0] + '\t' + check4[i].split('\t')[0])
for i in range(len(check5)):
    count=0
    if check5[i] not in user_list:
        if check5[i] in check1:
            count += 1
        if check5[i] in check2:
            count += 1
        if check5[i] in check3:
            count += 1
        if check5[i] in check4:
            count += 1
        if count >= 2:
            user_list.append(check5[i].split('\n')[0])
            user_list.append(check5[i].split('\t')[1].split('\n')[0] + '\t' + check5[i].split('\t')[0])

user_list = list(set(user_list))
for i in range(len(user_list)):
    ff.write("{0}\n".format(user_list[i]))

ff.close()