from flask import Flask
app = Flask(__name__)

#DB on server, only for demonstration
nikeToAdidas = [{'S':100,'M':50,'L':20},{'S':0,'M':800,'L':200},{'S':1,'M':5,'L':2}]

#if the brand is 'S' and the Typs is 'Adidas' should return 64
@app.route('localhost/<brand>/<productType>')
def recommend(brand,productType):
    Brand = str(brand)
    Type = str(productType)
    countSize = [0 for i in range(5)]
    if (Brand == "S" and Type == "Adidas"):
        number = 0
        dict = nikeToAdidas[location(Brand)] #should be replace with DB lists
        for key, value in dict.items():
            countSize[location(key)] += value
        # algorithm
        totalCount = int(sum(countSize))
        for i in range(5):
            sizeNum = (i + 1) * 20
            number += sizeNum * (countSize[i] / totalCount)
        return number #retun 64 if success
    return 0 #return 0 if fail


def translateSize(size):
    if (size == 'XS'):
        return 20
    if (size == 'S'):
        return 40
    if (size == 'M'):
        return 60
    if (size == 'L'):
        return 80
    if (size == 'Xl'):
        return 100

def location(size):
    return int((translateSize(size))/20)-1


# Brand = str('M')
# Type = str('Adidas')
# countSize = [0 for i in range(5)]
# if (Brand == 'M' and Type == 'Adidas'):
#     number = 0
#     dict = nikeToAdidas[1]
#     for key,value in dict.items():
#         countSize[location(key)] += value
#     #algorithem
#     totalCount = int(sum(countSize))
#     for i in range(5):
#         sizeNum = (i+1)*20
#         number += sizeNum * ( countSize[i] / totalCount)
#
# print(number)

# if __name__ =="__main__":
#     app.run(debug = True)

# @app.route('/')
# def index():
#     print ("hello world")