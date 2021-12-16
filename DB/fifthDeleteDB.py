# do not run this!
# deletes the DB
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="testforme"
)

mycursor = db.cursor()

mycursor.execute("DROP DATABASE testforme")

db.commit()
