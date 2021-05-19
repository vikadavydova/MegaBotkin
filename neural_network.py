import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import models
from tensorflow.keras import layers
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import tensorflow

import pandas

path = 'neural_network_datasets/'
dataframe_name = "data_valid_5"

df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False, index_col=0)
df.drop('DBD091', axis=1, inplace=True)
print(df.__contains__('DBD091'))

X = df.loc[:, df.columns != 'MCQ010']
y = df.loc[:, df.columns == 'MCQ010']

os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)




model = models.Sequential()
# Input - Layer
model.add(layers.Dense(400, activation = "sigmoid", input_shape=(62, )))
# Hidden - Layers
model.add(layers.Dense(400, activation = "sigmoid"))
model.add(layers.Dense(400, activation = "sigmoid"))
model.add(layers.Dense(400, activation = "sigmoid"))
# Output- Layer
model.add(layers.Dense(1, activation = "softmax"))
model.summary()

# compiling the model
model.compile(
 optimizer = "adam",
 loss = "binary_crossentropy",
 metrics = ["accuracy"]
)

results = model.fit(
 X_train, y_train,
 epochs= 2,
 batch_size = 32,
 validation_data = (X_test, y_test
))
print("Test-Accuracy:", np.mean(results.history["val_acc"]))