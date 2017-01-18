import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict


def day_price_predict():

    data = pd.read_csv("/home/metalm/Desktop/udacity/petr4/interday2.csv", decimal=',')

    print(data.head())

    #divide data in train and test

    X_train, X_test, y_train, y_test = train_test_split(data['day'], data['price'], test_size=0.5)
    
    X_train = X_train.values.reshape(len(X_train), 1)

    X_test = X_test.values.reshape(len(X_test), 1)

    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)


    print(clf.score(X_test, y_test))

    regr = linear_model.LinearRegression()

    regr.fit(X_test, y_test)

    plt.scatter(X_test, y_test, color='black')
    plt.scatter(X_train, y_train, color='red')
    plt.plot(X_test, regr.predict(X_test), color='blue', linewidth=1)
    plt.xticks(())
    plt.yticks(())
    plt.show()


day_price_predict()
