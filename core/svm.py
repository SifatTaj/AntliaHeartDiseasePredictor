from sklearn.svm import SVC

from core.model import x_train, y_train, x_test, y_test

svm = SVC(random_state = 1)
svm.fit(x_train.T, y_train.T)

acc = svm.score(x_test.T,y_test.T)*100

print("Test Accuracy of SVM Algorithm: {:.2f}%".format(acc))