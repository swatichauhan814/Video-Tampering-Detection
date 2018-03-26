import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
# fix random seed for reproducibility
numpy.random.seed(7)
filename = "updated_text.txt"
dataset = open(filename).read()
dataset = dataset.split("\n")
# print len(dataset)
L=[]
V=[]
for i in range(0, len(dataset) -1):
	line = dataset[i]
	X,Y=line.split(" ")
	lis=[]
	X=X.split(",")
	P=[]
	for x in X:
		if len(x)>0:
			P.append(int(x))
	X=[]

	ma=max(P)
	mi=min(P)
	ma=ma-mi
	ma=ma*1.0
	for x in P:
		u=float(x/ma)
		X.append(u)
	V.append(X)
	for y in Y:
		if len(y)>0:
			L.append(int(y))
	
Y=numpy.array(L, dtype=object)
X=numpy.array(V, dtype=object)
model = Sequential()
model.add(Dense(12, input_dim=5000, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
filepath="Results/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, Y, epochs=15, batch_size=10,callbacks=callbacks_list) 
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


filename = "test_data.txt"
dataset = open(filename).read()
dataset = dataset.split("\n")
# print len(dataset)
L_test=[]
V_test=[]
for i in range(0, len(dataset) -1):
	line = dataset[i]
	X_test,Y_test=line.split(" ")
	lis=[]
	X_test=X_test.split(",")
	for y in Y_test:
		if len(y)>0:
			L_test.append(int(y))
			
	P_test=[]
	for x in X_test:
		if len(x)>0:
			P_test.append(int(x))
	X_test=[]

	ma=max(P_test)
	mi=min(P_test)
	ma=ma-mi
	ma=ma*1.0
	for x in P_test:
		u=float(x/ma)
		X_test.append(u)
	# if len(X)!=4999:
		# print "Error"
	V_test.append(X_test)
Y_test=numpy.array(L_test, dtype=object)
X_test=numpy.array(V_test, dtype=object)

scores = model.evaluate(X_test, Y_test, verbose=0)
print scores
print("Accuracy: %.2f%%" % (scores[1]*100))