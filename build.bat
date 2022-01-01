@ECHO OFF
set /P passwd="Please enter your mysql password: "
cd DB
python firstLoadDB.py %passwd%
python secondLoadTable.py %passwd%
python thirdInjectData.py %passwd%
cd ..
cd client
npm install
exit