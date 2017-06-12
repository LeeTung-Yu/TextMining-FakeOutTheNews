#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Import data
from sklearn.datasets import load_files
data_folder = '/YOUR_DATA_DIRECTORY...'

dataset = load_files(data_folder, shuffle=False)

### Partition data
from sklearn.model_selection import train_test_split
docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=None)


############ SVM ############
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

svm_clf = Pipeline([('vect', TfidfVectorizer()),  # Feature Extraction
                     ('clf', SVC()),
])
svm_clf.fit(docs_train, y_train)

predicted_svm = svm_clf.predict(docs_test)
import numpy as np
np.mean(predicted_svm == y_test) 

from sklearn import metrics
print(metrics.classification_report(y_test, predicted_svm,
    target_names=dataset.target_names))

############ Decision Tree ############
from sklearn import tree
tree_clf = Pipeline([('vect', CountVectorizer()),
                     ('clf', tree.DecisionTreeClassifier()),
])
clf_fit = tree_clf.fit(docs_train, y_train)

predict_tree = clf_fit.predict(docs_test)
import numpy as np
np.mean(predict_tree == y_test) 

from sklearn import metrics
print(metrics.classification_report(y_test, predict_tree,
    target_names=dataset.target_names))


############ Logistic Regression ############
from sklearn.linear_model import LogisticRegression
log_clf = Pipeline([('vect', TfidfVectorizer()),
                     ('clf', LogisticRegression()),
])
log_model = log_clf.fit(docs_train, y_train)

predict_log = log_clf.predict(docs_test)
import numpy as np
np.mean(predict_log == y_test) 

from sklearn import metrics
print(metrics.classification_report(y_test, predict_log,
    target_names=dataset.target_names))
