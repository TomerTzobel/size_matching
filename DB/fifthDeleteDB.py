# do not run this!
# deletes the DB
import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd= str(sys.argv[1]),
    database="size_matching"
)

mycursor = db.cursor()

mycursor.execute("DROP DATABASE size_matching")

db.commit()
