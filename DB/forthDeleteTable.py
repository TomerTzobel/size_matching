import mysql.connector

# run this only if you want to delete the table for rerunning the tests

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="testforme"
)

mycursor = db.cursor()

mycursor.execute("DROP TABLE users_test")

db.commit()
