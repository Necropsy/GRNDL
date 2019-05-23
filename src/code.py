import tensorflow as tf
import GRN
import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

GRAPH = 21
EPOCHS = 1000

def base(NO):
    '''mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0'''
    grn = GRN.GRN(NO)
    dic["data"] = "labels"
    while(len(dic) < int(2**NUM_NOS/3)):
        key = str(rd.choices(range(2), k=21)).replace(", ", "")
        dic[key] = grn.atrator(key)
    dataframe = pd.DataFrame(data=dic)
    dataframe.rename({'col':'log(gdp)'}, axis=1)

def new_model():
    modelo = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(20, activation=tf.nn.relu, input_shape=(10,)),
        tf.keras.layers.Dense(20, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(10)
        ])
    optimizer = tf.train.RMSPropOptimizer(0.001)
    modelo.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
    
    return modelo

# Criando do modelo
model = new_model()

# Informações da estrutura do modelo
model.sumary()

# Visualizar o passar das épocas
class loading(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')

# Treinamento da Rede
history = model.fit(x_train, y_train, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[loading()])

def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [1000$]')
    plt.plot(history.epoch, np.array(history.history['mean_absolute_error']),
           label='Train Loss')
    plt.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
           label = 'Val loss')
    plt.legend()
    plt.ylim([0, 5])

plot_history(history)