
# Findtheroommate

## Project summary

### One-sentence description of the project

A web app for finding the roommate.

### Additional information about the project

TODO: Write a compelling/creative/informative project description / summary


## Installation

### Prerequisites

TODO:

### Installation Steps

Install the virtualenv first
If you are on Mac OS X or Windows, download get-pip.py, then:

```sudo python2 Downloads/get-pip.py
sudo python2 -m pip install virtualenv
```

Create an environment
Create a project folder and a venv folder within:

```
cd 5pm-findtheroommate
python3 -m venv venv
```

Activate the environment
Before you work on your project, activate the corresponding environment:

```
. venv/bin/activate
```

Install Flask
Within the activated environment, use the following command to install Flask:

```
python3 -m pip install Flask
```

Run the program
1. Open the terminal and type 'export FLASK_APP=hello.py'
2. Type 'export FLASK_ENV=development' (optional)
3. Type 'python3 -m flask run' to run the program


Deploy the app on Heroku
https://devcenter.heroku.com/articles/getting-started-with-python
1. Create the heroku account
2. Create a new project under your account
3. Deploy the app

    Log in to your Heroku account and follow the prompts to create new SSH public key.

        $ heroku login
        
    Clone the repository

    Use Git to clone findtheroommate's source code to your local machine.

        $ heroku git:clone -a findtheroommate
        $ cd findtheroommate
        
    Deploy your changes

    Make some changes to the code you just cloned and deploy them to Heroku using Git.

        $ git add .
        $ git commit -am "make it better"
        $ git push heroku master


## Functionality

TODO: Write usage instructions. Structuring it as a walkthrough can help structure this section,
and showcase your features.


## Known Problems

TODO: Describe any known issues, bugs, odd behaviors or code smells. 
Provide steps to reproduce the problem and/or name a file or a function where the problem lives.


## Contributing

TODO: Leave the steps below if you want others to contribute to your project.

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

If you haven't already, add a file called `LICENSE.txt` with the text of the appropriate license.
We recommend using the MIT license: <https://choosealicense.com/licenses/mit/>
