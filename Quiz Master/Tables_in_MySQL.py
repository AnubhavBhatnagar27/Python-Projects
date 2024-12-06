#Database and Table creation 
import mysql.connector as cntr 
db = cntr.connect(host = 'localhost' , user = 'root' , 
passwd = 'root') 
if db.is_connected(): 
    print('Connected Successfully!') 
cur = db.cursor() 
cur.execute("create database if not exists quiz") 
cur.execute("use quiz") 
cur.execute("create table question(qid integer(4),question varchar(500),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),ans varchar(100))") 
cur.execute("create table auth(username varchar(50),password varchar(50),category varchar(50))") 
print("Database and Tables created successfully") 
c = input("Press any key to continue-----> ") 
cur.close() 
db.close()