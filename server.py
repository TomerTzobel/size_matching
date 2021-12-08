import json
import mysql.connector

from flask import Flask,request
import pandas as pd
import numpy as np
app = Flask(__name__)
from flask_cors import CORS, cross_origin
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# instructions: change the password to the password that you chose for you own SQL
# then run only part 2 to create the DB
# once you did it, set back part 2 to comment and then run only part 1
db = mysql.connector.connect(
    host="localhost",
    user="root",
    #passwd="aaat", #our last name first char's, change it if you need
    passwd ="abc70807", # for tomer, need to stay in comment
    database="testforme" #part 1 - run after part 2
    )

mycursor = db.cursor() # making
# part 2 - run first and then set back to comment
# mycursor.execute("CREATE DATABASE testforme") #run only one time

#new table!!!!!!!!!!!!!!!!!!!
# mycursor.execute("CREATE TABLE users_test (user_id int PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(50), password VARCHAR(10), nike_shirt ENUM('S', 'M', 'L', 'XL'),"
#                "mango_shirt ENUM('S', 'M', 'L', 'XL'), gap_shirt ENUM('S', 'M', 'L', 'XL'),"
#                  "reebok_shirt ENUM('S', 'M', 'L', 'XL'), mango_dress ENUM('S', 'M', 'L', 'XL'), yanga_dress ENUM('S', 'M', 'L', 'XL'),"
#                  "reebok_jacket ENUM('S', 'M', 'L', 'XL'), adidas_jacket ENUM('S', 'M', 'L', 'XL'), mango_jacket ENUM('S', 'M', 'L', 'XL'),"
#                  "puma_jacket ENUM('S', 'M', 'L', 'XL'))")


# mycursor.execute("CREATE TABLE users (name VARCHAR(50), password VARCHAR(50),"
#                 "personID int PRIMARY KEY AUTO_INCREMENT)") #run only one time

#DB on server, only for demonstratcdion
nikeToAdidas = [{'S':100,'M':50,'L':20},{'S':0,'M':800,'L':200},{'S':1,'M':5,'L':2}]
passwordsDict = dict()

#if the brand is 'Adidas' and the Typs is 'shirt' should return 64
#for exmaple our host alreay buy nike shirt with size 'S' (index 1 in the array)
#among all the people that are size Small in Nike:
# 800 of them are size M in adidas
# 200 of them are size L in adids
# therefor we shuld get the number for recommend 64 (when 60 is M and 80 is L)
@app.route("/recommend/<string:brand>/<string:productType>")
@cross_origin()
def recommend(brand,productType):
    countSize = [0 for i in range(5)]
    if (productType == "shirt" and brand == "adidas"):
        number = 0
        dict = nikeToAdidas[1] #should be replace with DB lists
        for key, value in dict.items():
            countSize[location(key)] += value
        # algorithm
        totalCount = int(sum(countSize))
        for i in range(5):
            sizeNum = (i + 1) * 20
            number += sizeNum * (countSize[i] / totalCount)
        return str(number) #retun 64 if success
    return "0" #return 0 if fail

#in order to test use brand- nike and type-shirt
@app.route("/get/<string:brand>/<string:productType>")
@cross_origin()
def get(brand,productType):
    file = open("data.csv", "r")
    df = pd.read_csv(file)
    df = df[df.Type == productType]
    df = df[df.Brand == brand]
    d = df.transpose().to_dict(orient='dict')
    file.close()
    return d

@app.route("/get/<string:productType>")
@cross_origin()
def getbyword(productType):
    file = open("data.csv", "r")
    df = pd.read_csv(file)
    if productType in {"shirt","dress","jacket"}:
        df = df[df.Type == productType]
    else:
        df = df[df.Brand == productType]
    d = df.transpose().to_dict(orient='dict')
    file.close()
    return d

@app.route("/login", methods=["POST","GET"])
@cross_origin()
def login():
    if request.method == "POST":
        mycursor = db.cursor()
        dic = request.get_json(force=True)
        username = dic["username"]
        password = dic["password"]
        mycursor.execute("SELECT COUNT(*) FROM users_test WHERE (`user_name`) = %s", (str(username),))
        count = mycursor.fetchall()[0][0]
        if (count != 0): #if the user already exist
            # mycursor.execute("UPDATE users SET password = %s WHERE name = %s", (str(password),str(username)))
            return "0"
        else:
            mycursor.execute("INSERT INTO users_test (`user_name`, `password`) VALUES(%s, %s)", (str(username), str(password)))
        #print(f"registered new user: {username}, updates users dict: ")
        db.commit() #commit changes to our DB
        return "1"
    if request.method == "GET":
        mycursor = db.cursor()
        dic = request.args.to_dict()
        username = dic["username"]
        password = dic["password"]
        mycursor.execute("SELECT COUNT(*) FROM users_test WHERE (`user_name`) = %s", (str(username),))
        count = mycursor.fetchall()[0][0]
        if (count == 0):
            return "0"  # fail
        mycursor.execute("SELECT password FROM users_test WHERE user_name = %s", (str(username),))
        result = mycursor.fetchall()[0][0]
        if (result == password):
            return "1" #success
        return "0"

@app.route("/add",methods=["POST"])
@cross_origin()
def add():
    if request.method == "POST":
        mycursor = db.cursor()
        dic = request.get_json(force=True)
        user = dic["username"]
        size = dic["size"]
        brand = dic["brand"]
        type = dic["type"]
        column_name = brand+"_"+type
        mycursor.execute(f"UPDATE users_test SET {column_name} = %s WHERE `user_name` = %s", (str(size), str(user)))
        db.commit()
    return "1" #should always success

@app.route("/history/<string:user>")
@cross_origin()
def history(user):
    mycursor = db.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM users_test WHERE `user_name` = %s", (user,))
    dict = mycursor.fetchall()[0]
    del dict['user_id']
    del dict['user_name']
    del dict['password']
    dict = {k: v for k, v in dict.items() if v is not None}
    my_dict = {}
    i = 0
    for key in  dict:
        toAdd = {}
        values = key.split('_')
        toAdd['brand'] = values[0]
        toAdd['type'] = values[1]
        toAdd['size'] = dict[key]
        my_dict[i] = toAdd
        i += 1
    mycursor = db.cursor()
    db.commit()
    return my_dict


# @app.route("/add/<string:user>/<string:brand>/<string:productType>/<string:size>",methods=["POST","GET"])
# @cross_origin()
# def add(user,brand,productType,size):
#     # if request.method == "POST":
#     #     print("1")
#     #     return "1"
#     column_name = brand+"_"+productType
#     mycursor.execute(f"UPDATE users_test SET {column_name} = %s WHERE `user_name` = %s", (size, user))
#     # mycursor.execute("SELECT * FROM users_test")
#     # for x in mycursor:
#     #     print(x)
#     db.commit()
#     return "0"


# @app.route("/login", methods=["POST","GET"])
# @cross_origin()
# def login():
#     if request.method == "POST":
#         dic = request.get_json(force=True)
#         #dic = json.loads(dic)
#         username = dic["username"]
#         password = dic["password"]
#         #username = request.form.get("username")
#         #password = request.form.get("password")
#         print(username)
#         print(type(username))
#         passwordsDict.update({username:password})
#         print(f"registered new user: {username}, updates users dict: ")
#         print(passwordsDict)
#         return "1"
#     if request.method == "GET":
#         dic = request.args.to_dict()
#         #dic = json.loads(dic)
#         username = dic.get("username")
#         password = dic.get("password")
#         print(username)
#         print(type(username))
#         x = passwordsDict.get(username)
#         if (x == password):
#             return "1" #success
#         else:
#             return "0" #fail


def translateSize(size):
    if (size == "XS"):
        return 20
    if (size == "S"):
        return 40
    if (size == "M"):
        return 60
    if (size == "L"):
        return 80
    if (size == "Xl"):
        return 100
    else:
        return 0 #translate fail

def location(size):
    return int((translateSize(size))/20)-1

#to start the server
if __name__ =="__main__":
    app.run(debug = True)


# file = open("data.csv", "r")
# df = pd.read_csv(file)
# file.close()
# df = df[df.type == "shirt"]
# df = df[df.brand == "nike"]
# df = df.drop(["type", "brand"], axis=1)
# print(df)
# d = df.to_dict(orient='records')
# print(d)



# @app.route('/')
# def index():
#     return "hello world"

# brand = "shirt"
# productType = "adidas"
# countSize = [0 for i in range(5)]
# if (brand == "shirt" and productType == "adidas"):
#     number = 0
#     dict = nikeToAdidas[1] #should be replace with DB lists
#     for key, value in dict.items():
#         countSize[location(key)] += value
#     # algorithm
#     totalCount = int(sum(countSize))
#     for i in range(5):
#         sizeNum = (i + 1) * 20
#         print (sizeNum * (countSize[i] / totalCount))
#         number += sizeNum * (countSize[i] / totalCount)
#     print(number) #retun 64 if success
