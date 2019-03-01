# importing csv module
import csv
import mysql.connector


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
mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), Year VARCHAR(50), Dorm VARCHAR(50), Room VARCHAR(50), GPA VARCHAR(50))")



# reading csv file
with open(filename, "r") as csv_file:
    #creating a csv reader object
    csv_reader = csv.reader(csv_file)

    # A counter that will keep track of which line the program is on
    line_count=0

    # A for loop to traverse the lines in  the CSV file
    for row in csv_reader:
        if line_count==0:
            print(row[0] + " was in the year " + row[1] + " lived in " +  row[2] + " and graduated with a GPA of " + row[3])
            line_count +=1

        else:
            sql = "INSERT INTO students (name, year, dorm,room,GPA)VALUES (%s, %s, %s, %s, %s)"
            val = (row[0], row[1], row[2], row[3], row[4] )
            mycursor.execute(sql,val)
            mydb.commit()

#sql= "DROP TABLE students"
#mycursor.execute(sql)

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
