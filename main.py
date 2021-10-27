# What version of Python do you have?
import sys

import tensorflow.keras #import keras won't work we have to import keras as import tensorflow.keras to acess keras gpu processing library
import pandas as pd
import sklearn as sk
#metrics allows us to measure or calculate the accuracy of a ML model
from sklearn import datasets,preprocessing, svm, metrics #datasets can hold different types of datasets and svm is gonna be our classifier and preprocessing
from sklearn.neighbors import KNeighborsClassifier
import pickle
import tensorflow as tf
import numpy as np

import matplotlib.pyplot as pyplot #this module will help us to plot grid and visualize our dataset and stuff
from matplotlib import style #this is gonna change the style of our grid
import pickle #this module will help us to save our Ml model once the training is complete

print(f"Tensor Flow Version: {tf.__version__}")
print(f"tensor-flow (GPU): {tf.test.gpu_device_name()}") #check if the tensorflow gpu is installed or not
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"numpy {np.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")

# now that we've checked for the pakages and their version installed in the conda environment

#before we can use car.data we need to add attributes buying,maint,door,persons,lug_boot,safety,class on the first line in the file cars.data file
#so the reason we are doing this is because we need pandas to read this file and what padas does is that it reads the first line of any input file as an attribute or the features for the dataset
# so I have just defined what these attributes are by adding the line buying,maint,door,persons,lug_boot,safety,class on the first line in the file cars.data file

#now we can go ahead and read the cars.data file using pandas
#here we will be using read_csv even though it's not a csv file but the data inside this file is seperated by comma so we are going to use it
data = pd.read_csv("breast-cancer.data")

#just to ensure it's working I am going to go ahead and print out the data head here
print(data.head())

#We should generally avoid using attributes with non numerical data for example yes or no in it because we are performing computaion on this data and we are performing operations on them
#and we cannot do that on a non-numerical data of an attribute in a data file
#but here we are dealing with a data file in which most of the attributes that it's containing is of non-numerical type that means there is only one way to deal with it
#we need to convert the non numerical data into a numerical data in all the attributes of the data file that have them
#so inorder to convert all thoes non numerical attribute to numeric attribute we are going to use sklearn preprocessing for that
#vhigh,vhigh,2,2,small,low,unacc so here we are going to convert vhigh,vhigh,small,low,unacc into integer values that corresponds with the medium
#so all of our med = 1 low = 0 and high = 2 and the same thing for all other attributes as well and sklearn has a preprocessing module whch will help us to do that

#its gonna take the lables in our data with non integer data in it and encode it in their appropriate integer values
#not at this time this is just the object that will do this for us we haven't done it yet we need to pass our dataframe to it to actually do that
Preprocessing_data = preprocessing.LabelEncoder()
#create an list for each of our columns in the data preprocessing requires a list
#so we are going to read the data file using pandas
age = Preprocessing_data.fit_transform(list(data["age"]))
menopause = Preprocessing_data.fit_transform(list(data["menopause"]))
tumor_size = Preprocessing_data.fit_transform(list(data["tumor-size"]))
inv_nodes = Preprocessing_data.fit_transform(list(data["inv-nodes"]))
node_caps = Preprocessing_data.fit_transform(list(data["node-caps"]))
deg_malig = Preprocessing_data.fit_transform(list(data["deg-malig"]))
breast = Preprocessing_data.fit_transform(list(data["breast"]))
breast_quad = Preprocessing_data.fit_transform(list(data["breast-quad"]))
irradiat = Preprocessing_data.fit_transform(list(data["irradiat"]))
Class_ = Preprocessing_data.fit_transform(list(data["Class"]))

#after conversion is complete we need to add this back into our main list
#buying = Preprocessing_data.fit_transform(list(data["buying"])) is gonna return to us a numpy array
#so now that we have integers we can work with this data

#here create a predict variable (output after the training of our KNN ML model is complete
predict = "Class_"

X = list(zip(age, menopause, tumor_size, inv_nodes, node_caps, deg_malig, breast, breast_quad, irradiat))#attributes we will use zip to turn all of our attributes into one list
Y = list(Class_)#labels turn our class_ into a list

# now we are going to split X and Y arrays into 4 variables
# X test , Y test , X train and Y train
# here sk = sklearn
# so here essentially we are taking all of our attributes in X array and all of our labels that we are trying to predict and we are going to split them up into
# four different arrays
# x_train array is gonna be a section of X attribute array
# y_train array is gonna be a section of Y label array
# x_test, y_test arrays are our test data that we are gonna use to test the accuracy of our Ml model that we are gonna create
# now the way it works is if we trained the model every single bit of data that we have and it will simply just memorize it
# test_size = 0.1 is splitting 10% of our data into a test samples (x_test, y_test arrays) so that when we test of that and it's never seen that information before

# if you use x_train, y_train, x_test, y_test = sk.model_selection.train_test_split(X, Y, test_size = 0.4 )
# then it will throw an error Input contains NaN, infinity or a value too large for dtype('float64').
# change the above to this x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(X, Y, test_size = 0.4 ) and this will solve the issue
x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(X, Y, test_size=0.1)










# cancer_classifier.pickle used poly kernel to train 92%
# cancer_classifier2.pickle used linear kernel to train 92%
#cancer_classifier4.pickle is trained using my custome data in csv format
'''
best_SVC_ML_model_accuracy=0
for i in range(9999999):
    x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(X, Y, test_size=0.1)
    #implementing SVM Classifier
    #you can provide SVC with soft or hard margin and a kernel(function to transform a 2D plane to a 3D plane or an existing plane to a higher dimensional plane
    #kernel = linear or poly(polynomial) or sigmoid if nothing given then kernel is gonna default to rbf
    #with poly we can specify the degree of a polynomial svm.SVC(kernel="poly", degree=2)
    #svm.SVC(kernel="linear", C=2) here C=1 means soft margin and C=0 means hard margin No points will be allowed in beteen the margins of a hyperplane
    classifier = svm.SVC(kernel="poly", C=2)

    classifier.fit(x_train,y_train)

    #now we need to predict some data before we can give this model an accuracy score
    y_predict = classifier.predict(x_test)
    #calculate the accuracy of the ML model
    accuracy = metrics.accuracy_score(y_test,y_predict)
    # accuracy = classifier.score(x_test, y_test)
    # print(f"accuracy of the SVM model:- {accuracy}%")

    if best_SVC_ML_model_accuracy < accuracy:
        best_SVC_ML_model_accuracy=accuracy
        print(f"best_SVC_ML_model_accuracy = {best_SVC_ML_model_accuracy}%")

        # saving the trained Ml model after the training is complete using pickle module that comes built in with python programming language
        # saving a trained Ml model is important because every time we train our model the accuracy of our Ml model fluctuates between 80 to 90 %
        # so we need to have the ability to save the Ml model with the highest accuracy so that we can use it in other projects to solve real world problems in our other projects
        # with open("studentmodel.pickle", "wb") it is gonna open a pickle file named studentmodel in wb mode and write the file if it doesn't already exists
        # pickle.dump(Linear, f)  this will save the opened pickle file if not already exists in our working projects directory , NOTE:->here Linear is our actual ML model
        with open("cancer_classifier4.pickle", "wb") as f:
            pickle.dump(classifier, f)
'''




#actual answers
classes = ['no-recurrence-events', 'recurrence-events']
#read in our pickle file
# open("studentmodel.pickle", "rb") this will open the pickle file studentmodel.pickle in our directory in rb mode
pickle_in = open("cancer_classifier4.pickle", "rb")

# once the pickle studentmodel.pickle is stored we can open the trained Ml model in form of studentmodel.pickle file we can just load this pickle in to our Linear variable
# which we will use as a trained ML model
#and use the trained ML model stored in form of pickle file to predict the student's final grade G3
classifier = pickle.load(pickle_in)

#getting the accuracy of our trained ML model
#now we need to predict some data before we can give this model an accuracy score
y_predict = classifier.predict(x_test)
accuracy = metrics.accuracy_score(y_test,y_predict)
print(f"accuracy of the trained SVM Ml model:==> {accuracy}%")

#here I am gonna print out all the predictions and then I am gonna show what the input data was for that predictions
# x_test array is the set of data on which our model is not trained
#printing the inputs to the Ml model
for x in range(len(y_predict)):
    print(f"input data : {x_test[x]}")
    print(f"SVM Ml model predictions : {classes[round(y_predict[x])]}")
    print(f"actual value answers : {classes[y_test[x]]}")