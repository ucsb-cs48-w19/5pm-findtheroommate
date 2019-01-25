How to run the 'hello world' flask app

##Install the virtualenv first
If you are on Mac OS X or Windows, download get-pip.py, then:

```sudo python2 Downloads/get-pip.py
sudo python2 -m pip install virtualenv
```

##Create an environment
Create a project folder and a venv folder within:

```
mkdir myproject
cd myproject
python3 -m venv venv
```

##Activate the environment
Before you work on your project, activate the corresponding environment:

```
. venv/bin/activate
```

##Install Flask
Within the activated environment, use the following command to install Flask:

```
pip install Flask
```

##Run the program
1. Open the terminal and type 'export FLASK_APP=hello.py'
2. Type 'export FLASK_ENV=development' (optional)
3. Type 'flask run' to run the program
