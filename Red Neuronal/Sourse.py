import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles

# CREAr EL DATASET
n = 500 # numero de registros que tenemos en niestro dato.
p = 2 # cuantas caracteristicas tenemos sobre cada uno de nuestros registros de nuestro dato.

X, Y = make_circles(n_samples=n, factor=0.5, noise=0.05)  # en este caso el eje Y es un vector Binario
plt.scatter(X[Y == 0, 0], X[Y == 0, 1], c = "skyblue")
plt.scatter(X[Y == 1, 0], X[Y == 1, 1], c = "salmon")
plt.axis("equal")
#plt.show()

# DEFINIMOS LA ESTRUCTURA DE DATOS QUE CONTIENE LOS PARAMETROS LE LA RED NEURONAL
#   CLASE DE LA CAPA DE LA RED
class neural_layer():
    def __init__(self, n_conn, n_neur, act_f):
        self.act_f = act_f
        
        # en este caso nos interesa que la inicializacion aleatoria de la red neuronal en torno a la media cero, es decir, que esté normalizada y estandarizada.  
        self.b = np.random.rand(1, n_neur) * 2 - 1 # se inicializa entre los valores (-1,1)    
        self.w = np.random.rand(n_conn, n_neur) * 2 - 1 # esto es una matriz

# FUNCIONES DE ACTIVACION

sigm = lambda x: 1 / (1 + np.e ** (-x)) # implementamos la funcion sigmoide
_x = np.linspace(-5, 5, 100)
plt.plot(_x, sigm(_x))


