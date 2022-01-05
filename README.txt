In order to run the project you need to download the following libraries for Python:
- mysql.connector, numpy, pandas
- Flask,request (from flask)
- CORS, cross_origin (from flask_cors)

also you need to download:
- node.js
- mySql

Easy run (for windows):
- build (only for the first run)
- run

Manual run:
build data (only in the first run)-
enter DB folder and then run by this order:
firstLoadDB.py 
secondLoadTable.py
thirdInjectData.py

build clilent-
enter client folder and run: npm install

run project-
run server.py
enter client folder and run: npm start

*please note that at each run of the server/build data, 
the password for your mySql should be provided as an argument