import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat", #our last name first char's
    database="testforme"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testforme")

#mycursor.execute("DROP TABLE users_test")

mycursor.execute("CREATE TABLE users_test (user_id int PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(50), password VARCHAR(10), nike_shirt ENUM('S', 'M', 'L', 'XL'),"
               "mango_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), gap_shirt ENUM('S', 'M', 'L', 'XL'),"
                 "reebok_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), anthropologie_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), yanga_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
                 "only_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
                 "mango_dress ENUM('S', 'M', 'L', 'XL'), yanga_dress ENUM('S', 'M', 'L', 'XL'), only_dress ENUM('S', 'M', 'L', 'XL'),"
                 "anthropologie_dress ENUM('S', 'M', 'L', 'XL'), guess_dress ENUM('S', 'M', 'L', 'XL'), glamorous_dress ENUM('S', 'M', 'L', 'XL'),"
                 "reebok_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), adidas_jacket ENUM('S', 'M', 'L', 'XL'), mango_jacket ENUM('S', 'M', 'L', 'XL'),"
                 "puma_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), only_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), gap_jacket ENUM('XS', 'S', 'M', 'L', 'XL'))")
