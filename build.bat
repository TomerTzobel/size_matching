@ECHO OFF
cd DB
python firstLoadDB.py
python secondLoadTable.py
python thirdInjectData.py
cd ..
cd client
npm install
exit