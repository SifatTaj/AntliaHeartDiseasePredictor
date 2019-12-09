from sklearn.tree import DecisionTreeClassifier

from core.model import x_train, y_train, x_test, y_test

dtc = DecisionTreeClassifier()
dtc.fit(x_train.T, y_train.T)

# acc = dtc.score(x_test.T, y_test.T)*100
# print("Decision Tree Test Accuracy {:.2f}%".format(acc))