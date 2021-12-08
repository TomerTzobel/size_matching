import mysql.connector
import string
import random
from enum import Enum

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat", #our last name first char's
    database="testforme"
    )

mycursor = db.cursor()
#mycursor.execute("CREATE DATABASE testforme")
#mycursor.execute("CREATE TABLE users_test (user_id int PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(50), password VARCHAR(10), nike_shirt ENUM('S', 'M', 'L', 'XL'),"
#                 "mango_shirt ENUM('S', 'M', 'L', 'XL'), gap_shirt ENUM('S', 'M', 'L', 'XL'),"
#                 "reebok_shirt ENUM('S', 'M', 'L', 'XL'), mango_dress ENUM('S', 'M', 'L', 'XL'), yanga_dress ENUM('S', 'M', 'L', 'XL'),"
#                 "reebok_jacket ENUM('S', 'M', 'L', 'XL'), adidas_jacket ENUM('S', 'M', 'L', 'XL'), mango_jacket ENUM('S', 'M', 'L', 'XL'),"
#                 "puma_jacket ENUM('S', 'M', 'L', 'XL'))")

shirts = ["nike_shirt", "mango_shirt", "gap_shirt", "reebok_shirt"]
dresses = ["mango_dress", "yanga_dress"]
jackets = ["reebok_jacket", "adidas_jacket", "mango_jacket", "puma_jacket"]
sizes = ['S', 'M', 'L', 'XL']

first_names = ["Shachar", "Hadas", "Yuval", "Orit", "Hani", "Daniel", "Noa", "Rina", "Amira", "Maya", "Ruth", "Dina", "Sharon", "Sara", #you can add name if you like
               "Roni", "Lihi", "Kim", "Shir", "Orna", "Rachel", "Dona", "Yasmin", "Michal", "Tamar", "Shani", "Galit", "Samira", "Qamar"
               "Dana", "Avivit", "Noy", "Rotem", "Hadar", "Shaked", "Monica", "Sara", "Shaked", "carmella", "Dvora", "Gitit"]
last_names = ["James", "Levi", "Cohen", "Robinson", "Jordan", "Golan", "Zait", "Mizrahi", "Yasin", "Brown", "Peretz", "Israeli", "Smith", #you can add name if you like
              "Barak", "Narkis", "Obama", "Hassan", "Diab", "Klein", "Sade", "Zisman", "Dor", "Chen", "Azaria", "Baron", "Clooney",
              "Akirov", "Gold", "Zuckerberg", "Clinton", "Rosen", "Alperon", "Kennedy", "Shuster", "Jameson", "Levin", "Sapir"]
full_names = []
count = 0
while(count < 10): #change to the number of women we want to insert the DB
    name = random.choice(first_names) + "_" + random.choice(last_names)
    if(name not in full_names):
        count += 1
        new_password = ''.join(random.choices(string.ascii_letters + string.digits,
                                          k=10))  # makes a random string with upper and lower cases and digits, size of 10.

        mycursor.execute("INSERT INTO users_test (user_name, password) VALUES(%s, %s)", (name, new_password))



db.commit()

mycursor.execute("SELECT * FROM users_test")
for x in mycursor:
    print(x)

