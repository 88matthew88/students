import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database= "mydatabase"
)

mycursor = mydb.cursor()

Query =  r""" LOAD DATA LOCAL INFILE 'C:\Users\Mcfarlane.m\Desktop\Python\Test-file.csv'
            INTO TABLE students
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            ESCAPED BY '"'
            Lines terminated by '\n'
            IGNORE 1 LINES """

mycursor.execute(Query)
connection.commit()

#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


cursor.close()
