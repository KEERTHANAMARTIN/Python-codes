import mysql.connector
conn= mysql.connector.connect(host="localhost",database="employee1",
                              user="root",password="keerthi")
cursor = conn.cursor()
print(conn.is_connected())

mysql = "select * from employee_details"
cursor.execute(mysql)  #cursor - that blinking in sql ,here we are trying to execute the cursor
rows =cursor.fetchall()
print(rows)