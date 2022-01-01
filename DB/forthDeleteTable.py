import mysql.connector
import sys

# run this only if you want to delete the table for rerunning the tests

db = mysql.connector.connect(
    host="localhost",
    user="root",
    # passwd="aaat", #our last name first char's
    passwd=str(sys.argv[1]),
    database="size_matching"
)

mycursor = db.cursor()

mycursor.execute("DROP TABLE users")

db.commit()
