import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="testforme"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE users_test (user_id int PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(50) NOT NULL, password VARCHAR(10) NOT NULL, nike_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
               "mango_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), gap_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "reebok_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), anthropologie_shirt ENUM('XS', 'S', 'M', 'L', 'XL'), yanga_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "only_shirt ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "mango_dress ENUM('XS', 'S', 'M', 'L', 'XL'), yanga_dress ENUM('XS', 'S', 'M', 'L', 'XL'), only_dress ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "anthropologie_dress ENUM('XS', 'S', 'M', 'L', 'XL'), guess_dress ENUM('XS', 'S', 'M', 'L', 'XL'), glamorous_dress ENUM('XS', 'S', 'M', 'L', 'XL'),"
                 "gap_dress ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "reebok_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), adidas_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), mango_jacket ENUM('XS', 'S', 'M', 'L', 'XL'),"
                "puma_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), only_jacket ENUM('XS', 'S', 'M', 'L', 'XL'), gap_jacket ENUM('XS', 'S', 'M', 'L', 'XL'))")

db.commit()