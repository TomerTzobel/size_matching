@ECHO OFF
set /P passwd="Please enter you mysql password: "
start python server.py %passwd%
cd client
start npm start
exit