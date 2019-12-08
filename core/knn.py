from sklearn.neighbors import KNeighborsClassifier

import model

knn = KNeighborsClassifier(n_neighbors=2)  # k=2
knn.fit(model.x_train.T, model.y_train.T)
prediction = knn.predict(model.x_test.T)

print(model.x_test.T)
print(model.x_test)
print (type(model.x_test))

print(prediction)

# print("{} NN Score: {:.2f}%".format(2, knn.score(x_test.T, y_test.T) * 100))