import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd= str(sys.argv[1]),
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE size_matching")