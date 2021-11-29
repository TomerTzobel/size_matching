import json

from flask import Flask,request
import pandas as pd
import numpy as np
app = Flask(__name__)
from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    df = df.drop(["Type", "Brand"], axis=1)
    d = df.transpose().to_dict(orient='dict')
    file.close()
    return d

@app.route("/login/", methods=["POST","GET"])
@cross_origin()
def login():
    if request.method == "POST":
        content = request.get_json(force=True)
        dic = json.loads(content)
        username = dic["username"]
        password = dic["password"]
        #username = request.form.get("username")
        #password = request.form.get("password")
        passwordsDict.update({username:password})
    if request.method == "GET":
        contant = request.get_json(force=True)
        dic = json.loads(contant)
        if (username not in passwordsDict):
            return "0"
        username = dic.get("username")
        password = dic.get("password")
        x = passwordsDict.get(username)
        if (x == password):
            return "1" #success
        else:
            return "0" #fail

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
