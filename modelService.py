from sklearn import svm
import pandas
import numpy as np
import pickle

classifier = None

def get_model():
    global classifier
    if classifier:
        return classifier
    else:
        try:
            __get_pickle()
            return classifier
        except Exception as e:
            print(e)
            __build_pickle()
            return classifier

def __build_pickle():
    global classifier
    classifier = svm.SVC(kernel='linear')
    train = pandas.read_csv("train.csv",encoding='utf-8')
    train_X,train_Y = pre_process(train,train=True)
    classifier.fit(train_X, train_Y)
    file_model = open('model.obj', 'wb') 
    pickle.dump(classifier, file_model)

def __get_pickle():
    global classifier
    filehandler = open('model.obj', 'rb') 
    classifier = pickle.load(filehandler)

def __normalize_port(value):
    if value == 'S':
        return 0
    if value == 'C':
        return 1
    if value == 'Q':
        return 2
    if np.isnan(value):
        return 3
    raise Exception("Invalid input: port colum | "+str(value))

def __normalize_sex(value):
    if value == 'male':
        return 0
    if value == 'female':
        return 1
    raise Exception("Invalid input: sex colum | "+str(value))

def __normalize_age(value):
    if np.isnan(value):
        return 0
    return value

def __normalize_fare(value):
    if np.isnan(value):
        return 0
    return value

def pre_process(data,train=False):
    X = data
    del X['Name']
    del X['Ticket']
    del X['Cabin']
    del X['PassengerId']
    X['Embarked'] = X['Embarked'].apply(__normalize_port)
    X['Sex'] = X['Sex'].apply(__normalize_sex)
    X['Age'] = X['Age'].apply(__normalize_age)
    X['Fare'] = X['Fare'].apply(__normalize_fare)
    if train:
        Y = data['Survived']
        del X['Survived']
        return X,Y
    else:
        return X





