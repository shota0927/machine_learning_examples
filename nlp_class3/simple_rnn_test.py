# https://deeplearningcourses.com/c/deep-learning-advanced-nlp
from __future__ import print_function, division
from builtins import range, input
# Note: you may need to update your version of future
# sudo pip install -U future

from keras.models import Model
from keras.layers import Input, LSTM, GRU
import numpy as np
import matplotlib.pyplot as plt


T = 8
D = 2
M = 3


X = np.random.randn(1, T, D)


def lstm1():
  input_ = Input(shape=(T, D))
  rnn = LSTM(M, return_state=True)
  x = rnn(input_)

  model = Model(inputs=input_, outputs=x)
  o, h, c = model.predict(X)
  print("o:", o)
  print("h:", h)
  print("c:", c)


def lstm2():
  input_ = Input(shape=(T, D))
  rnn = LSTM(M, return_state=True, return_sequences=True)
  # rnn = GRU(M, return_state=True)
  x = rnn(input_)

  model = Model(inputs=input_, outputs=x)
  o, h, c = model.predict(X)
  print("o:", o)
  print("h:", h)
  print("c:", c)


def gru1():
  input_ = Input(shape=(T, D))
  rnn = GRU(M, return_state=True)
  x = rnn(input_)

  model = Model(inputs=input_, outputs=x)
  o, h = model.predict(X)
  print("o:", o)
  print("h:", h)


def gru2():
  input_ = Input(shape=(T, D))
  rnn = GRU(M, return_state=True, return_sequences=True)
  x = rnn(input_)

  model = Model(inputs=input_, outputs=x)
  o, h = model.predict(X)
  print("o:", o)
  print("h:", h)



print("lstm1:")
lstm1()
print("lstm2:")
lstm2()
print("gru1:")
gru1()
print("gru2:")
gru2()


