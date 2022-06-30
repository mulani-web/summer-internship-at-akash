import mysql.connector
k = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database = "mydb"
)

mycursor = k.cursor()
#sql = "INSERT INTO tbl_student (`st_name`, `st_email`, `st_mob`) VALUES ('komal', 'komal.mulani123@gmail.com', '7046818101')"
mycursor.execute("SELECT * FROM tbl_student")
#k.commit()
#print(mycursor.rowcount ,"row inserted")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)