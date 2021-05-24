import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import confusion_matrix
import scikitplot as skplt


path = 'logistic_regression_datasets/'
dataframe_name = "data_lr_5_fit"

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

df = pd.read_csv(f"{path}{dataframe_name}", low_memory=False, index_col=0)
df = clean_dataset(df)
print(df)
X = df.loc[:, df.columns != 'MCQ010']
y = df.loc[:, df.columns == 'MCQ010']


os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns

os_data_X, os_data_y = os.fit_resample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X, columns=columns )
os_data_y = pd.DataFrame(data=os_data_y, columns=['MCQ010'])

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)
logmodel = LogisticRegression(max_iter=2000)
logmodel.fit(os_data_X, os_data_y.values.ravel())

predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))
confusion_matrix(y_test, predictions)

y_probas = logmodel.predict_proba(X_test)# predicted probabilities generated by sklearn classifier
skplt.metrics.plot_roc(y_test, y_probas, plot_micro=False, plot_macro=False, classes_to_plot=1,
                       title='Logistics regression')
plt.savefig('logreg.png')
plt.show()



