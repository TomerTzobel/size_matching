import mysql.connector
import string
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="testforme"
)

def choose_size(size):
    if size == 'XS':
        possible_sizes = ['XS', 'S']
        return random.choices(possible_sizes, weights=(75, 25), k=1)
    if size == 'S':
        possible_sizes = ['XS', 'S', 'M']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)
    if size == 'M':
        possible_sizes = ['S', 'M', 'L']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)
    if size == 'L':
        possible_sizes = ['M', 'L', 'XL']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)
    if size == 'XL':
        possible_sizes = ['L', 'XL']
        return random.choices(possible_sizes, weights=(25, 75), k=1)
    raise Exception("wrong input")

def update_db(brands, number_of_purchases, size, name):
    for i in range(number_of_purchases):
        chosen_size = choose_size(size)
        sqlCommand = "UPDATE users_test SET " + brands[i] + "=%s WHERE user_name=%s"
        sqlVars = (chosen_size[0], name)
        mycursor.execute(sqlCommand, sqlVars)

mycursor = db.cursor()

shirts = ["nike_shirt", "mango_shirt", "gap_shirt", "reebok_shirt", "anthropologie_shirt", "yanga_shirt", "only_shirt"]

dresses = ["mango_dress", "yanga_dress", "only_dress", "gap_dress", "anthropologie_dress", "guess_dress",
           "glamorous_dress"]

jackets = ["reebok_jacket", "adidas_jacket", "mango_jacket", "puma_jacket", "only_jacket", "gap_jacket"]

sizes = ['XS', 'S', 'M', 'L', 'XL']

first_names = ["Shachar", "Hadas", "Yuval", "Orit", "Hani", "Daniel", "Noa", "Rina", "Amira", "Maya", "Ruth", "Dina",
               "Sharon", "Sara", "Nofar", "Tanya", "Anna", "Anat", "Yael", "Johanna",  # you can add names if you like
               "Roni", "Lihi", "Kim", "Shir", "Orna", "Rachel", "Dona", "Yasmin", "Michal", "Tamar", "Shani", "Galit",
               "Samira", "Qamar", "Nasrin", "Dana", "Avivit", "Noy", "Rotem", "Hadar", "Shaked", "Monica", "Sara", "Shaked",
               "carmella", "Dvora", "Gitit", "Nadin", "Taylor", "Jessica"]

last_names = ["James", "Levi", "Cohen", "Robinson", "Jordan", "Golan", "Zait", "Mizrahi", "Yasin", "Brown", "Peretz",
              "Israeli", "Smith", "Rubinshtein", "Silver", "Mazor", "Yamin", # you can add names if you like
              "Barak", "Narkis", "Obama", "Hassan", "Diab", "Klein", "Sade", "Zisman", "Dor", "Chen", "Azaria", "Baron",
              "Clooney", "Bennet",
              "Akirov", "Gold", "Zuckerberg", "Clinton", "Rosen", "Alperon", "Kennedy", "Shuster", "Jameson", "Levin",
              "Sapir", "Dean", "Shelbi", "Jaber"]

full_names = []
count = 0

while (count < 500):  # change to the number of women we want to insert the DB
    name = random.choice(first_names) + "_" + random.choice(last_names)
    if name not in full_names:
        count += 1
        new_password = ''.join(random.choices(string.ascii_letters + string.digits,
                                              k=10))  # makes a random string with upper and lower cases and digits, size of 10.
        mycursor.execute("INSERT INTO users_test (user_name, password) VALUES(%s, %s)", (name, new_password))

        number_of_shirt_purchases = random.randint(2, 4)
        number_of_dress_purchases = random.randint(2, 4)
        number_of_jacket_purchases = random.randint(2, 4)

        shirt_size = random.choice(sizes)
        dress_size = random.choice(sizes)
        jacket_size = random.choice(sizes)

        chosen_shirt_brands = random.sample(shirts, number_of_shirt_purchases)
        chosen_dress_brands = random.sample(dresses, number_of_dress_purchases)
        chosen_jacket_brands = random.sample(jackets, number_of_jacket_purchases)

        update_db(chosen_shirt_brands, number_of_shirt_purchases, shirt_size, name)
        update_db(chosen_dress_brands, number_of_dress_purchases, dress_size, name)
        update_db(chosen_jacket_brands, number_of_jacket_purchases, jacket_size, name)

db.commit()
mycursor.execute("SELECT * FROM users_test")
for x in mycursor:
    print(x)
