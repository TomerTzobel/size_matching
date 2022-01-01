@ECHO OFF
set /P passwd="Please enter your mysql password: "
start python server.py %passwd%
cd client
start npm start
exit