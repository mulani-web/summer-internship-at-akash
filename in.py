import mysql.connector
k = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database = "mydb"
)

mycursor = k.cursor()
sql = "INSERT INTO tbl_student (`st_name`, `st_email`, `st_mob`) VALUES ('anita', 'anita.mulani123@gmail.com', '9904037171')"
mycursor.execute(sql)
k.commit()
print(mycursor.rowcount ,"row inserted")

