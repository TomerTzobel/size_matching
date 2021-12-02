import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat", #our last name first char's
    database="testforme"
    )

mycursor = db.cursor() # making
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

a = 26
mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Avi", 28))
mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Tomer", a))
mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Adam", 27))
mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Amit", 27))

db.commit()


mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)