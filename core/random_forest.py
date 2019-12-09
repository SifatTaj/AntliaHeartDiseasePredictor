from core.model import x_train, y_train, x_test, y_test

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=1000, random_state=1)
rf.fit(x_train.T, y_train.T)

# acc = rf.score(x_test.T, y_test.T) * 100
# print("Random Forest Algorithm Accuracy Score : {:.2f}%".format(acc))
