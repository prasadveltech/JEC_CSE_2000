import matplotlib.pyplot as plt
import numpy as np


###--------------------------------JEC CSE 1996 - 2000's Code----------------------------------------------------###

print('Enter path to your file:')
file = input()
print("JEC CSE 2000 Whatsapp Chat Analytics")
f = open(file, encoding="utf8")

k = list()
admins = set()
timestamp = []  # '-' splitted
msglog = []  # '-' splitted
date = []  # ',' splitted
time = []  # ',' splitted

###----------------------------------------------------###
###			following code to split and store data		###
for i in f.readlines():
    if i.find("changed the subject to ") != -1:
        continue
    k.append(i.split('--'))

# timestamp=[]
# msglog=[]
for i in k:
    # print('i in k value is ',i)
    # print('i in k length of i is ',len(i))
    if (len(i) >= 2):
        if i[0].count('/') == 2 and i[0].count(',') != 0:
            # timestamp.append(i[0])
            temp = ''
            for k in range(1, len(i)):
                temp += i[k]
            if temp.find(':') != -1:
                msglog.append(temp)
                timestamp.append(i[0])
            elif temp.find('added') != -1:
                admins.add(temp[:temp.find('added')])
            elif temp.find('created') != -1:
                admins.add(temp[:temp.find('created')])

        else:
            temp = ''
            temp += msglog[len(msglog) - 1]
            temp += '\n' + i[0]
            msglog[len(msglog) - 1] = temp
    else:
        temp = ''
        # print(len(msglog))
        temp += msglog[len(msglog) - 1]
        temp += '\n' + i[0]
        msglog[len(msglog) - 1] = temp

# date=[]
# time=[]
# print('timestamp is ',timestamp)
for i in timestamp:
    temp = i.split(',')
    date.append(temp[0].split('[')[1])
    time.append(temp[1])
###----------------------------------------###



###---------------------------------------------------------------------------###
###			following code to split msglog to store users and messages and for most active user		###
users = set()  # to store phoneno.
users_cnt = {}  # string--->list...phoneno--->list of its messages
for i in msglog:
    contact = ''
    ind = i.index(':')
    # if ind != 0:
    # print(":ind {}".format(i.index(':')))
    contact += i[:ind]
    # print("Contact {}".format(contact))
    users.add(contact.strip)
    if users_cnt.get(contact, -1) == -1:
        users_cnt[contact] = []
    users_cnt[contact].append(i[ind + 1:])
###--------------------------------------------------------------------------###



###-------------------------------------------------------------------------------------###
### 			following code for pie chart of top 10 users  			###
nmsg_per_user = {}
for i in users_cnt:
    nmsg_per_user[i] = len(users_cnt[i])
sorted_users_cnt = sorted(nmsg_per_user, key=nmsg_per_user.__getitem__, reverse=True)
top_5_users = []

print('sorted_users_cnt =>', sorted_users_cnt)
print('nmsg_per_user =>', nmsg_per_user)
for i in range(15):
    top_5_users.append([sorted_users_cnt[i], nmsg_per_user[sorted_users_cnt[i]]])  # [user,no. f msg by him/her]
plt.pie([i[1] for i in top_5_users], labels=[i[0] for i in top_5_users], startangle=90, shadow=True, autopct='%1.1f%%')

plt.title('Top 15 Active Users....!!!')
plt.legend(loc=(.65, -0.12))
# plt.legend(loc=(.78,-0.12))
plt.show()
###-----------------------------------------------------------------------------------------###


###-------------------------------------------------------------------------------------###
### 			following code for pie chart of top 10 users  - new style			###
nmsg_per_user = {}
for i in users_cnt:
    nmsg_per_user[i] = len(users_cnt[i])
sorted_users_cnt = sorted(nmsg_per_user, key=nmsg_per_user.__getitem__, reverse=True)
top_10_users = []

# print('sorted_users_cnt =>',sorted_users_cnt)
# print('nmsg_per_user =>',nmsg_per_user)
for i in range(10):
    top_10_users.append([sorted_users_cnt[i], nmsg_per_user[sorted_users_cnt[i]]])  # [user,no. f msg by him/her]
data = [i[1] for i in top_10_users]
label = [i[0] for i in top_10_users]


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:d} msgs".format(absolute)


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, label,
          title="Top 10 Active Users !",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

plt.show()
###-----------------------------------------------------------------------------------------###


###-------------------------------------------------------------------------------------###
### 			following code for pie chart of least 10 users  - new style			###
nmsg_per_user = {}
for i in users_cnt:
    nmsg_per_user[i] = len(users_cnt[i])
sorted_users_cnt = sorted(nmsg_per_user, key=nmsg_per_user.__getitem__, reverse=False)
least_10_users = []

# print('sorted_users_cnt =>',sorted_users_cnt)
# print('nmsg_per_user =>',nmsg_per_user)
for i in range(10):
    least_10_users.append([sorted_users_cnt[i], nmsg_per_user[sorted_users_cnt[i]]])  # [user,no. f msg by him/her]
data = [i[1] for i in least_10_users]
label = [i[0] for i in least_10_users]


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:d} msgs".format(absolute)


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, label,
          title="Top 10 Inactive Users!",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

plt.show()
###-----------------------------------------------------------------------------------------###


f.close()




