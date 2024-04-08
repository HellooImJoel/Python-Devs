# Importar las bibliotecas necesarias
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import pandas as pd

# Crear el modelo
modelo = Sequential()

# Añadir la capa de entrada y la primera capa oculta
modelo.add(Dense(32, input_dim=8, activation='relu'))

# Añadir la segunda capa oculta
modelo.add(Dense(16, activation='relu'))

# Añadir la capa de salida
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Aquí puedes entrenar el modelo con tus datos
# modelo.fit(X_train, y_train, epochs=150, batch_size=10)

# Cargar los datos
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
nombres = ['num_pregnant', 'glucose_concentration', 'blood_pressure', 'skin_thickness', 'serum_insulin', 'BMI', 'pedigree_function', 'age', 'class']
datos = pd.read_csv(url, names=nombres)

# Dividir los datos en características (X) y etiquetas (y)
X = datos.iloc[:,0:8]
y = datos.iloc[:,8]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
modelo = Sequential()
modelo.add(Dense(12, input_dim=8, activation='relu'))
modelo.add(Dense(8, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=150, batch_size=10, verbose=0)

# Hacer una predicción
predicciones = modelo.predict_classes(X_test)

# Imprimir las primeras 5 predicciones
print(predicciones[:5])






