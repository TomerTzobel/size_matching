@ECHO OFF
set /P passwd="Please enter you mysql password: "
cd DB
python firstLoadDB.py %passwd%
python secondLoadTable.py %passwd%
python thirdInjectData.py %passwd%
cd ..
cd client
npm install
exit