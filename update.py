import mysql.connector
k = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database = "mydb"
)

mycursor = k.cursor()
sql = "UPDATE tbl_student SET `st_name`= 'komal' WHERE st_id = 1"
mycursor.execute(sql)
k.commit()
print(mycursor.rowcount ,"row updated")

