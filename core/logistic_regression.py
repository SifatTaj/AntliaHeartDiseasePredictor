from sklearn.linear_model import LogisticRegression

from core.model import x_train, y_train, x_test, y_test

lr = LogisticRegression()
lr.fit(x_train.T, y_train.T)

print (lr.predict(x_test.T))

acc = lr.score(x_test.T, y_test.T) * 100
print("Test Accuracy {:.2f}%".format(acc))
