#!/usr/bin/python3
import pymysql
conn = pymysql.connect(host='123.57.241.125', port=3306,
                       user='pyuser', charset='utf8', passwd='7PVFy34O', db='pytest')
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print("MySQL server version:", row[0])
cursor.close()
conn.close()
