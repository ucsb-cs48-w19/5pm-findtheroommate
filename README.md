## Findtheroommate
## Project summary
## One-sentence description of the project

    A web app for UCSB students to find the next great roommate.

## Additional information about the project

    Did you get a summer internship in a far away city that you feels exicited about? Congrats! Wow, now you have to think about housing. See there is not many good options out there for you. Airbnb is affordable, but do you really wanna live with strangers AND their family? You can look on craglist to find roommates for apartment, but how much trust should you give to the strangers behind the computer screen in a remote city? Renting a studio/apartment by yourself, Sure! Just not much money left after you have worked very hard while your friends are enjoying the beach and the sunlight.
    This is when you turn to find-the-roommate for help! As a UCSB student, say for some reasons (eg. internship, travel) that you need to live in New York for the summer, you can use our app to make a post and find fellow Gauchos who is also interested in New York. Then you can meet them in person, and interact! And you repeat this process until you find the one :) Now you can be assured that you will live with someone you know is not a creep, and clicked with you nicely!

## Installation
## Prerequisites

    You have a computer that runs on either Mac, Window, or Linux.
    installed git
    Installed Python 3.7.2
    Installed flask (through command line, see instructions below)

## Installation Steps

### Download python3.7.1
    Download python from python.org

### Create virtualenv
macos:
```
python3 -m venv myvenv
windows:
py -m venv myvenv
```
### Activate virtualenv
windows:
```
venv\Scripts\activate
macos:
venv/bin/activate
```

### Download package from requirements
```
pip install -r requirements.txt
if failed, use --user flag
```

### Run locally
```
flask run
```

### Deploy on pythonanywhere
    Create a pythonanwhere account on website www.pythonanywhere.com
    Open a console and git clone the repo using http.
    Create virtualenv:
    ```
    mkvirtualenv myvirtualenv --python=/usr/bin/python3.7
    ```
    Now leave the console and click the web button.
    Found the code part
    Turn source code to absolute path of the git repo with the directory 5pm-findtheroommate/app
    Click the WSGI configuration file
    Decomment codes part of flask
    Change the value of path to the absolute path of the repo(same as source code).
    change from flask_app ... to from app...
    change the virtulenv path to home/username/.virtualenvs/myvirtualenv
## Functionality

    MVP product

## Known problems

    Describe any known issues, bugs, odd behaviors or code smells. Provide steps to reproduce the problem and/or name a file or a function where the problem lives.

## Contributing

        Fork it!
        Create your feature branch: git checkout -b my-new-feature
        Commit your changes: git commit -am 'Add some feature'
        Push to the branch: git push origin my-new-feature
        Submit a pull request :D

## License

    If you haven't already, add a file called LICENSE.txt with the text of the appropriate license. We recommend using the MIT license: https://choosealicense.com/licenses/mit/
