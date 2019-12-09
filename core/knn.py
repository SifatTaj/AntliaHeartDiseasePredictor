from sklearn.neighbors import KNeighborsClassifier

from core import model

knn = KNeighborsClassifier(n_neighbors=3)  # k=3
knn.fit(model.x_train.T, model.y_train.T)

# prediction = knn.predict(model.x_test.T)

# print(model.x_test.T)
# print(model.x_test)
# print (type(model.x_test))

# print(prediction)

# print("{} NN Score: {:.2f}%".format(2, knn.score(x_test.T, y_test.T) * 100))