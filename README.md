# size_matching
Project, E-Commerce workshop

In order to run the project you need to download the following libraries for Python:
- mysql.connector, numpy, pandas
- Flask, request (from flask)
- CORS, cross_origin (from flask_cors)

also you need to download:
- Node.js
- MySql

Easy run (for windows):
- build (only for the first run)
- run

Manual run:

build data (only in the first run):

enter DB folder and then run by this order:
- firstLoadDB.py 
- secondLoadTable.py
- thirdInjectData.py

build clilent (only in the first run):
- enter client folder and run: npm install

run project-
- run server.py
- enter client folder and run: npm start

*please note that at each run of the server/build data, 
the password for your mySql should be provided as an argument


Note - after buying an item there's a 5s timeout. Please *wait for it* and don't buy another product before the feedback form appears (we assumed 'normal' behavior by users). 

Adam Kroskin- 314050683
Avi Kashani- 204159438
Amit Sharon- 205372485
Tomer Tzobel- 208468538
