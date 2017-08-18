
import numpy as np
from numpy import newaxis
import keras
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, LSTM, TimeDistributed
import pandas as pd

def init():
    global trainedmod
    from keras.models import load_model
    
    trainedmod = load_model("finalmodel.sav")
def run(npa):
    global trainedmod
    
    if (len(npa.shape) > 1):
        ypred = trainedmod.predict(npa.reshape(npa.shape[0],24,1))
    else:
        ypred = trainedmod.predict(npa.reshape(1,24,1))
    retdf = pd.DataFrame(data={"Scored Values":np.squeeze(np.reshape(ypred, newshape= [-1,1]), axis=1)})
    return str(retdf)