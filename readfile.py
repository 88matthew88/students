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



# reading csv file
with open(filename, "r") as csv_file:
    #creating a csv reader object
    csv_reader = csv.reader(csv_file)

    # get field names
    # fields = csvreader.next()
    # A counter that will keep track of which line the program is on
    line_count=0

    # A for loop to traverse the lines in  the CSV file
    for row in csv_reader:

        #Checking to see if the loop is on the first line
        if line_count==0:
            print("Column names are : " + row[0]+ row[1] + row[2] + row[3])

            #increments the line count
            line_count += 1
        else:
            print(row[0] + " was in the year " + row[1] + " lived in " +  row[2] + " and graduated with a GPA of " + row[3])
            line_count += 1

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# create student table
mycursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(50), Year VARCHAR(50), Dorm VARCHAR(50), Room VARCHAR(50), GPA VARCHAR(50))")
