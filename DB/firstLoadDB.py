import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat", #our last name first char's
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE size_matching")