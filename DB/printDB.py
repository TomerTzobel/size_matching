import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    #passwd="aaat", #our last name first char's
    passwd= str(sys.argv[1]),
    database="size_matching"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM users")
for x in mycursor:
    print(x)