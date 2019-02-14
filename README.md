












## download python3.7.1
download python from python.org

## create virtualenv
macos:
python3 -m venv myvenv
windows:
py -m venv myvenv
## activate virtualenv
windows:
venv\Scripts\activate
macos:
venv/bin/activate

## download package from requirements
pip install -r requirements.txt
if failed, use --user flag

## run locally
flask run

## deploy on pythonanywhere
create a pythonanwhere account on website www.pythonanywhere.com
open a console and git clone the repo using http.
create virtualenv:
mkvirtualenv myvirtualenv --python=/usr/bin/python3.7
now leave the console and click the web button
found the code part
turn source code to absolute path of the git repo with the directory 5pm-findtheroommate
click the WSGI configuration file
decomment codes part of flask
change the value of path to the absolute path of the repo(same as source code).



