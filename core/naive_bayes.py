from sklearn.naive_bayes import GaussianNB

from model import x_train, y_train, x_test, y_test

nb = GaussianNB()
nb.fit(x_train.T, y_train.T)

acc = nb.score(x_test.T, y_test.T)*100
print("Accuracy of Naive Bayes: {:.2f}%".format(acc))