git add --all

@echo off
cls 
set /p msg="Enter message: "

git commit -m "%msg%"
git push -u origin master
pause