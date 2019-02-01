# Findtheroommate
## Project summary
### One-sentence description of the project  
* A web app for UCSB students to find the next great roommate.
### Additional information about the project  
* Did you get a summer internship in a far away city that you feels exicited about? Congrats! Wow, now you have to think about housing. See there is not many good options out there for you. Airbnb is affordable, but do you really wanna live with strangers AND their family? You can look on craglist to find roommates for apartment, but how much trust should you give to the strangers behind the computer screen in a remote city? Renting a studio/apartment by yourself, Sure! Just not much money left after you have worked very hard while your friends are enjoying the beach and the sunlight. 
* This is when you turn to find-the-roommate for help! As a UCSB student, say for some reasons (eg. internship, travel) that you need to live in New York for the summer, you can use our app to make a post and find fellow Gauchos who is also interested in New York. Then you can meet them in person, and interact! And you repeat this process until you find the one :) Now you can be assured that you will live with someone you know is not a creep, and clicked with you nicely!  
 
 
## Installation
### Prerequisites  
* You have a computer that runs on either Mac, Window, or Linux.
* installed [git](https://git-scm.com/downloads) 
* Installed [Python 3.7.2](https://www.python.org/downloads/)
* Installed flask (through command line, see instructions below)
### Installation Steps  
* Installed Python 3  
    * go to https://www.python.org/downloads/, and click download python 3.7.2
    * make sure you check the box for pip in optional features, and check the box for "add Python to environment variable" in advanced options"  
* Configure Virtual Environment  
    * venv is a built-in program for virtual environment that comes with installing python 3.7.2
    * in your terminal, after you are in the directory where you want the folder for this app exist, type in the following one by one
    ```mkdir find-the-roommate
        cd find-the-roommate
        python3 -m venv venv
    ```
    * if you are using windows instead of Mac/Linux, swap out the third line above to 
    ```py -3 -m venv venv``` 
* Activate the environment  
    * right now you should be inside the folder named find-the-roommate
    * type in your terminal the following command  
    ```. venv/bin/activate```
    * if you are using windows instead of Mac/Linux, do the below instead
    ```venv\Scripts\activate```
    * now you should see (venv) before your normal terminal prompt  

* Installed flask
    * stay where you are, and type
    ```pip install flask```
    * if the above do not work, try this instead
    ```python -m pip install flask```

* Run the program  
    * after succesful installation of flask, type the below, and hit enter
    ```python hello.py```
    * We currently use hello.py as a place holder for the real files
    * You should see "running on http://....."
    * Open a new web browser, and paste whatever is after the word on into the url area
    * At this point, you should see "Hello World" on the screen

## Functionality

* Display "hello World"

## known problems
* TODO: Describe any known issues, bugs, odd behaviors or code smells. Provide steps to reproduce the problem and/or name a file or a function where the problem lives.

## Contributing

* TODO: Leave the steps below if you want others to contribute to your project.  
    * Fork it!
    * Create your feature branch: git checkout -b my-new-feature
    * Commit your changes: git commit -am 'Add some feature'
    * Push to the branch: git push origin my-new-feature
    * Submit a pull request :D

## License

* If you haven't already, add a file called LICENSE.txt with the text of the appropriate license. We recommend using the MIT license: https://choosealicense.com/licenses/mit/
