# Titanic Survival API

## Introduction

> This is an Flask, python 3 API exposing a service that allows anyone to input personal data and see if they would have survived the Titanic accident.
The data used to build the model was the kaggle competition [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

>We used Scikit learn's linear SVC to build a machine learning model using the train data provided in that competition.


>The service runs at Heroku: https://titanic-survival-model-api.herokuapp.com/predict, but can run in any terminal with python 3 installed.

## Model reasoning

The data has 10 meaningful fields and 1 identification field.
We disregard the following fields:
* 'Name'
* 'Ticket'
* 'Cabin'

and then proceed with a number of basic data cleanup on the remaining fields before constructing the model.
The model object is saved in a file in order to save time on start up. If a model.obj is present, the API will not build the model again, but use the saved one.


## Request example

> This is a request example using curl:

curl --location --request POST 'https://titanic-survival-model-api.herokuapp.com/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "PassengerId": 892,
    "Pclass": 1,
    "Name": "Kelly, Mr. James",
    "Sex": "female",
    "Age": 34.5,
    "SibSp": 0,
    "Parch": 0,
    "Ticket": 330911,
    "Fare": 700.8292,
    "Cabin": "",
    "Embarked": "Q"
}'

The response is [1] for a positive result (survived) and [0] for a negative (not surived).

The project also contains the file **serviceCaller.py** which is also used to make a request to the service.

**All fields are mandatory**

## Installation

1. install requirements

>pip install requirements.txt



2. run flask

>set FLASK_APP=hello

>flask run

## Improvements

* Add enpoint to force a new model fit
* Normalize all the data
* Include last names in the model
* Include feature (is cabin present)
* Include feature (does ticket has letter)
