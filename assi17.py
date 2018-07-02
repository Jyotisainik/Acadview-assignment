#1.
import pymysql
db=pymysql.connect('localhost','root','system','demo')
cursor=db.cursor()
qr1="create table book(bookid int(2),titleid int(5),location char(20),genre char(10))"
qr2="create table title(titleid int(2),title char(20),IDSN int(5),publisherid int(7),publicationyear int(7))"
qr3="create table publishers(publishersid int(2),name char(20),streetaddress char(20),suitenumber int(5),zipcodeid int(7))"
qr4="create table zip code(zipcodeid int(2),city char(20),state char(20),zipcode int(5))"
qr5="create table authors title(authortitleid int(5),authorid int(5),titleid int(5))"
qr6="create table authors(authorid int(5),firstname char(20),middlename char(20),lastname char(10))"
cursor.execute(qr1)
cursor.execute(qr2)
cursor.execute(qr3)
cursor.execute(qr4)
cursor.execute(qr5)
cursor.execute(qr6)
db.close()

#2.
db=pymysql.connect('localhost','root','system','demo')
cursor=db.cursor()
qr1="insert into book1 values(104,109,'haryana','ninth')"
qr2="insert into title values(106,'c++',999,657,1985)"
qr3="insert into publishers values(101,'bjarne stroustrup','new york',201,13425)"
qr4="insert into zip_codes values(109 ,'kurkshetra','haryana',136118)"
qr5="insert into  Authors_title values(105,111,108)"
qr6="insert into Authors values(102,'Jyoti' ,'Saini','Kalanori')"
try:
    cursor.execute(qr1)
    cursor.execute(qr2)
    cursor.execute(qr3)
    cursor.execute(qr4)
    cursor.execute(qr5)
    cursor.execute(qr6)
    db.commit()
except:
    db.rollback()
db.close()

#3.
db=pymysql.connect('localhost','root','system','demo')
cursor=db.cursor()
qr1="select * from title"
qr2="update title set title = '2states' where titleid=101"
cursor.execute(qr)
print(cursor.fetchall())
try:
    crsor.execute(qr2)
    db.commit()
except:
    db.rollback()
cursor.execute(qr1)

db.close()
