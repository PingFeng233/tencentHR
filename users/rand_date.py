import time
import random
import sqlite3


# 生成随机日期
def rand_data():
    a = (2017, 6, 1, 0, 0, 0, 0, 0, 0)
    b = (2018, 4, 11, 0, 0, 0, 0, 0, 0)

    start = time.mktime(a)
    end = time.mktime(b)

    t = random.randint(start, end)
    data_toupe = time.localtime(t)
    date = time.strftime('%Y-%m-%d', data_toupe)
    return date


conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

# conn.execute('CREATE TABLE test (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT)')
for i in range(1, 221):
    date = rand_data()
    cur.execute('UPDATE zhaopin_zhaopin SET publishTime="%s" where id=%d' % (date, i))
    conn.commit()
    print(date)
