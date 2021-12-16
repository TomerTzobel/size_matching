# do not run this!
# deletes the DB
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="size_matching"
)

mycursor = db.cursor()

mycursor.execute("DROP DATABASE size_matching")

db.commit()
