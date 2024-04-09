import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# Creamos nuestros datos artificiales
X, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

# Definimos el modelo
model = Sequential()
model.add(Dense(16, input_shape=(2,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilamos el modelo
model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])

# Entrenamos el modelo
model.fit(X, Y, epochs=100)

# Predecimos con el modelo
predictions = model.predict(X)

# Visualizamos los resultados
plt.scatter(X[:,0], X[:,1], c=predictions[:,0], cmap='bwr')
