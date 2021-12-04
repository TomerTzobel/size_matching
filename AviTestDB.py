import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat", #our last name first char's
    #passwd ="abc" for tomer
    database="testforme"
    )

mycursor = db.cursor() # making
# mycursor.execute("CREATE DATABASE testforme")
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# a = 26
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Avi", 28))
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Tomer", a))
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Adam", 27))
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Amit", 27))
#
# db.commit()

# mycursor.execute("CREATE TABLE shirts (name VARCHAR(50), "
#                  "nike VARCHAR(2),"
#                  "adidas VARCHAR(2),"
#                  "mango VARCHAR(2), "
#                  "personID int PRIMARY KEY AUTO_INCREMENT)")

#mycursor.execute("INSERT INTO shirts (name, nike,adidas,mango) VALUES(%s, %s, %s, %s)", ("Avi", "L","M","M"))
# mycursor.execute("INSERT INTO shirts (name, nike,adidas,mango) VALUES(%s, %s, %s, %s)", ("tomer", "L","S","S"))
# mycursor.execute("INSERT INTO shirts (name, nike,adidas,mango) VALUES(%s, %s, %s, %s)", ("adam", "L","Xl","XL"))
# mycursor.execute("INSERT INTO shirts (name, nike,adidas,mango) VALUES(%s, %s, %s, %s)", ("amit", "M","M","M"))

db.commit()
mycursor.execute("SELECT * FROM shirts")
for x in mycursor:
    print(x)

size = "L"
brand = "adidas"
size = repr(str(size))
mycursor.execute("SELECT %s FROM shirts WHERE nike = %s" % (brand,size))
for x in mycursor:
    print(x[0])



mycursor.execute("SHOW TABLES")
for table_name in mycursor:
   print(table_name)

mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)