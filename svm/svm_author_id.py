#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm
# clf = svm.SVC(kernel='linear')  # accuracy = 0.616
# clf = svm.SVC(kernel='rbf', C=10.0)  # accuracy = 0.616
# clf = svm.SVC(kernel='rbf', C=100.0)  # accuracy = 0.616
# clf = svm.SVC(kernel='rbf', C=1000.0)  # accuracy = 0.821
clf = svm.SVC(kernel='rbf', C=10000.0)  # accuracy = 0.892
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

t1 = time()
predictions = clf.predict(features_test)
print "prediction time:", round(time() - t1, 3), "s"

print "prediction for element 10:", predictions[10]
print "prediction for element 26:", predictions[26]
print "prediction for element 50:", predictions[50]

import collections
counts = collections.Counter(predictions)
print "number of times chris is predicted:", counts[1]

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, predictions)
print "accuracy is:", accuracy
#########################################################


