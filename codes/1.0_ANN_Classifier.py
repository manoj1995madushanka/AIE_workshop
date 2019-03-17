# toy dataset included to scify
from sklearn import datasets #importing datasets from sklearn
import numpy as np

iris = datasets.load_iris() #getting the iris flower dataset into iris

#check whether dataset loaded
#print(iris)

data = iris.data #data features 150*4 2D array
target = iris.target  #target labels 150 1d array

#check whether data loaded
#print(data)
#print(iris)

train_data = np.delete(data, [0,50,100], axis=0) #delete unvanted data use axis fordelete rows not columns

#print(train_data)

train_target = np.delete(target,[0,50,100])

#print(train_target)

from sklearn.neighbors import KNeighborsClassifier

clsfr = KNeighborsClassifier() #loading the KNN to clsfr
#KNN is somtypes of brain in MLwe can use another types as well

#training beginning line below line is execute training process using provided data
clsfr.fit(train_data,train_target) # training the KNN model

#introduce test_data to early removed data
test_data = data[[0,50,100]]
test_target = target[[0,50,100]]

#print(test_data)


#now test it works using we early removed data
result = clsfr.predict(test_data)

print("predicted result : " ,result)