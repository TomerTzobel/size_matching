import json
import mysql.connector
import sys

from flask import Flask,request
import pandas as pd
import numpy as np
app = Flask(__name__)
from flask_cors import CORS, cross_origin
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
app.config['CORS_HEADERS'] = 'Content-Type'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd= str(sys.argv[1]),  # our last name first char's, change it if you need
    #passwd="aaat", #our last name first char's, change it if you need
    #passwd ="abc70807", # for tomer, need to stay in comment
    database="size_matching"
    )

mycursor = db.cursor() #making

@app.route("/recommend/<string:user>/<string:brand>/<string:productType>")
@cross_origin()
def recommend(user,brand,productType):
    value = 0
    column_name = brand + "_" + productType
    dictSizes = build_dict(user,column_name,productType)
    if (isinstance(dictSizes, int)): #the user already bought a product of the same type and brand
        return str(dictSizes)
    #algorithm
    totalCount = 0
    for size in dictSizes:
        totalCount += int(dictSizes[size])
    if(totalCount == 0): #not enough data
        return "-1"
    for size in dictSizes:
        sizeNum = translateSize(size)
        value += sizeNum * (dictSizes[size] / totalCount)
    return str(value)


def build_dict(user,column_name,productType):
    sizeDict = {'XS':0,'S':0,'M':0,'L':0,'XL':0}
    mycursor = db.cursor(dictionary=True)
    try:
        mycursor.execute("SELECT * FROM users WHERE `user_name` = %s", (user,))
    except:
        try:
            mycursor.execute("SELECT * FROM users WHERE `user_name` = %s", (user,))
        except:
            print("error in server")
            return None
    historyDict = mycursor.fetchall()[0]
    if (historyDict[column_name] != None): #the user already buy product from the same type and brand
        size = historyDict[column_name]
        return translateSize(size)
    historyDict = {k: v for k, v in historyDict.items() if v is not None}
    del historyDict['user_id']
    del historyDict['user_name']
    del historyDict['password']
    mycursor = db.cursor()
    for brandKey in historyDict:
        size_for_brandKey = historyDict[brandKey]
        x = brandKey.split("_")
        if (x[1] != productType): #make sure we count only the shopping history from the same product type
            continue
        for sizeKey in sizeDict:
            try:
                mycursor.execute(f"SELECT COUNT(*) FROM users WHERE {brandKey} = %s AND {column_name} = %s",
                                 (str(size_for_brandKey), str(sizeKey)))
            except:
                try:
                    mycursor.execute(f"SELECT COUNT(*) FROM users WHERE {brandKey} = %s AND {column_name} = %s",
                                     (str(size_for_brandKey), str(sizeKey)))
                except:
                    print("error in server")
                    return None
            count = mycursor.fetchall()[0][0]
            sizeDict[sizeKey] += int(count)
    return sizeDict


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
        try:
            mycursor.execute("SELECT COUNT(*) FROM users WHERE (`user_name`) = %s", (str(username),))
        except:
            try:
                mycursor.execute("SELECT COUNT(*) FROM users WHERE (`user_name`) = %s", (str(username),))
            except:
                print("error in server")
                return None
        count = mycursor.fetchall()[0][0]
        if (count != 0): #if the user already exist
            return "0"
        else:
            try:
                mycursor.execute("INSERT INTO users (`user_name`, `password`) VALUES(%s, %s)",
                                 (str(username), str(password)))
            except:
                try:
                    mycursor.execute("INSERT INTO users (`user_name`, `password`) VALUES(%s, %s)",
                                     (str(username), str(password)))
                except:
                    print("error in server")
                    return None
        db.commit() #commit changes to our DB
        return "1"
    if request.method == "GET":
        mycursor = db.cursor()
        dic = request.args.to_dict()
        username = dic["username"]
        password = dic["password"]
        try:
            mycursor.execute("SELECT COUNT(*) FROM users WHERE (`user_name`) = %s", (str(username),))
        except:
            try:
                mycursor.execute("SELECT COUNT(*) FROM users WHERE (`user_name`) = %s", (str(username),))
            except:
                print("error in server")
                return None
        count = mycursor.fetchall()[0][0]
        if (count == 0):
            return "0"  # fail
        try:
            mycursor.execute("SELECT password FROM users WHERE user_name = %s", (str(username),))
        except:
            try:
                mycursor.execute("SELECT password FROM users WHERE user_name = %s", (str(username),))
            except:
                print("error in server")
                return None
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
        brand = brand.lower()
        type = type.lower()
        column_name = brand+"_"+type
        try:
            mycursor.execute(f"UPDATE users SET {column_name} = %s WHERE `user_name` = %s", (str(size), str(user)))
        except:
            try:
                mycursor.execute(f"UPDATE users SET {column_name} = %s WHERE `user_name` = %s", (str(size), str(user)))
            except:
                print("error in server")
                return None
        db.commit()
    return "1" #should always success

@app.route("/history/<string:user>")
@cross_origin()
def history(user):
    mycursor = db.cursor(dictionary=True)
    try:
        mycursor.execute("SELECT * FROM users WHERE `user_name` = %s", (user,))
    except:
        try:
            mycursor.execute("SELECT * FROM users WHERE `user_name` = %s", (user,))
        except:
            print("error in server")
            return None
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

def translateSize(size):
    if (size == "XS"):
        return 0
    if (size == "S"):
        return 25
    if (size == "M"):
        return 50
    if (size == "L"):
        return 75
    if (size == "XL"):
        return 100
    else:
        return 0 #translate fail, should always succeed

#to start the server
if __name__ =="__main__":
    app.run(debug = True)