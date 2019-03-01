# importing csv module
import csv
import mysql.connector

# initialize titles and rows list
#fields = []
#rows = []

#csv file name
filename = "Test-file.csv"

#Creating a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database= "mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# create student table
mycursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(50), Year VARCHAR(50), Dorm VARCHAR(50), Room VARCHAR(50), GPA VARCHAR(50))")


# reading csv file
with open(filename, "r") as csv_file:
    #creating a csv reader object
    csv_reader = csv.reader(csv_file)

    # get field names
    # fields = csvreader.next()

    # A for loop to traverse the lines in  the CSV file
    for row in csv_reader:
        print(row[0] + " was in the year " + row[1] + " lived in " +  row[2] + " and graduated with a GPA of " + row[3])
        #mycursor.executemany('INSERT into %s VALUES(%s, %s, %s, %s, %s)'%students, row)
        
        sql = "INSERT INTO students (name, year, dorm,room,GPA)VALUES (%s, %s, %s, %s, %s)"
        val = (row[0], row[1], row[2], row[3], row[4] )
        mycursor.execute(sql,val)
        mydb.commit()
        
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
