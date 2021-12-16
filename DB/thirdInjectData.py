import mysql.connector
import string
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="aaat",  # our last name first char's
    database="size_matching"
)


def get_bigger_size(size):
    if size == 'XS':
        return 'S'
    if size == 'S':
        return 'M'
    if size == 'M':
        return 'L'
    return 'XL'  # if size == 'XL' or 'L' returns 'XL'


def get_smaller_size(size):
    if size == 'M':
        return 'S'
    if size == 'L':
        return 'M'
    if size == 'XL':
        return 'L'
    return 'XS'  # if size == 'XS' or 'S' returns 'XS'


def check_if_small_or_big_brand(size, brand):
    brand = brand.split('_')[0]
    if brand == "mango":
        return get_bigger_size(size)
    if brand == "gap":
        return get_smaller_size(size)
    return size


def choose_size(size, brand):
    size = check_if_small_or_big_brand(size, brand)
    if size == 'XS':
        possible_sizes = ['XS', 'S']
        return random.choices(possible_sizes, weights=(75, 25), k=1)[0]
    if size == 'S':
        possible_sizes = ['XS', 'S', 'M']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)[0]
    if size == 'M':
        possible_sizes = ['S', 'M', 'L']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)[0]
    if size == 'L':
        possible_sizes = ['M', 'L', 'XL']
        return random.choices(possible_sizes, weights=(20, 60, 20), k=1)[0]
    if size == 'XL':
        possible_sizes = ['L', 'XL']
        return random.choices(possible_sizes, weights=(25, 75), k=1)[0]
    raise Exception("wrong input")


def update_db(brands, number_of_purchases, size, name):
    for i in range(number_of_purchases):
        chosen_size = choose_size(size, brands[i])
        sql_command = "UPDATE users SET " + brands[i] + "=%s WHERE user_name=%s"
        sql_vars = (chosen_size, name)
        mycursor.execute(sql_command, sql_vars)


mycursor = db.cursor()

shirts = ["nike_shirt", "mango_shirt", "gap_shirt", "reebok_shirt", "anthropologie_shirt", "yanga_shirt", "only_shirt"]

dresses = ["mango_dress", "yanga_dress", "only_dress", "gap_dress", "anthropologie_dress", "guess_dress",
           "glamorous_dress"]

jackets = ["reebok_jacket", "adidas_jacket", "mango_jacket", "puma_jacket", "only_jacket", "gap_jacket"]

sizes = ['XS', 'S', 'M', 'L', 'XL']

first_names = ["Shachar", "Hadas", "Yuval", "Orit", "Hani", "Daniel", "Noa", "Rina", "Amira", "Maya", "Ruth", "Dina", # you can add names if you like
               "Sharon", "Sara", "Nofar", "Tanya", "Anna", "Anat", "Yael", "Johanna", "Mary", "Jennifer", "Linda",
               "Roni", "Lihi", "Kim", "Shir", "Orna", "Rachel", "Dona", "Yasmin", "Michal", "Tamar", "Shani", "Galit",
               "Samira", "Qamar", "Nasrin", "Dana", "Avivit", "Noy", "Rotem", "Hadar", "Shaked", "Monica", "Sara",
               "Shaked", "Elizabeth", "Barbara", "Susan", "Nancy", "Lisa", "Betty", "Margaret", "Sandra", "Ashley"
               "carmella", "Dvora", "Gitit", "Nadin", "Taylor", "Jessica", "Emily", "Victoria"]

last_names = ["James", "Levi", "Cohen", "Robinson", "Jordan", "Golan", "Zait", "Mizrahi", "Yasin", "Brown", "Peretz", # you can add names if you like
              "Israeli", "Smith", "Rubinshtein", "Silver", "Mazor", "Yamin", "Anderson", "Thomas", "Moore", "Jackson",
              "Barak", "Narkis", "Obama", "Hassan", "Diab", "Klein", "Sade", "Zisman", "Dor", "Chen", "Azaria", "Baron",
              "Clooney", "Bennet", "Johnson", "Williams", "Jones", "Garcia", "Miller", "Davis", "David", "Wilson",
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
        mycursor.execute("INSERT INTO users (user_name, password) VALUES(%s, %s)", (name, new_password))

        number_of_shirt_purchases = random.randint(2, 4)
        number_of_dress_purchases = random.randint(2, 4)
        number_of_jacket_purchases = random.randint(2, 4)

        size = random.choice(sizes)
        # shirt_size = random.choice(sizes)
        # dress_size = random.choice(sizes)
        # jacket_size = random.choice(sizes)

        chosen_shirt_brands = random.sample(shirts, number_of_shirt_purchases)
        chosen_dress_brands = random.sample(dresses, number_of_dress_purchases)
        chosen_jacket_brands = random.sample(jackets, number_of_jacket_purchases)

        update_db(chosen_shirt_brands, number_of_shirt_purchases, size, name)
        update_db(chosen_dress_brands, number_of_dress_purchases, size, name)
        update_db(chosen_jacket_brands, number_of_jacket_purchases, size, name)

db.commit()

mycursor.execute("SELECT * FROM users")
for x in mycursor:
    print(x)
