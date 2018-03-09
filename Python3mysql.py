#!/usr/bin/python3
import pymysql
import os
import configparser
import date
 
CONFIG_FILE = "dbconfig.cfg"

#def main():
print(os.path.join(os.getcwd(), CONFIG_FILE))
if os.path.exists(os.path.join(os.getcwd(), CONFIG_FILE)):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    #第一个参数指定要读取的段名，第二个是要读取的选项名
    host = config.get("DB_Config", "DATABASE_HOST")
    port = config.get("DB_Config", "DATABASE_PORT")
    dbname = config.get("DB_Config", "DATABASE_NAME")
    username = config.get("DB_Config", "DATABASE_USERNAME")
    password = config.get("DB_Config", "DATABASE_PASSWORD")
    #print(host, port, dbname, username, password)


conn = pymysql.connect(host=host, port=int(port),
                       user=username, charset='utf8', passwd=password, db=dbname)
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()


try:
    with conn.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(
            sql, ('Robin', 'Zhyea', 'tomorrow', 'M', date(1989, 6, 14)))
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    conn.commit()

finally:
    conn.close()

print("MySQL server version:", row[0])
cursor.close()
conn.close()
