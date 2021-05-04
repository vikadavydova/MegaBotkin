import pandas
import openpyxl
import os
import fsspec
import pathlib
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

path = 'csv_datasets/'
dataframe_name = "data_valid_5"

test = pathlib.Path().absolute()
print(test)

df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False, index_col=0)
#list = df.columns.to_list()
#remove_list = ['SMDUPCA']
#result_list = [i for i in list if i in remove_list]
#print(df['MCQ010'].value_counts())
#df.loc[df['MCQ010'] == 2, 'MCQ010'] = 0
#df.drop(result_list, axis=1, inplace=True)
#print(df)
#print(test.count())
#df.to_csv(f"{path}data_valid_5")
list_cat_vars =[]
for name in df.columns:
    if (df[name].value_counts().count() > 2):
        list_cat_vars.append(name)


print(len(list_cat_vars))

cat_vars = list_cat_vars
for var in cat_vars:
    cat_list = 'var' + '_' + var
    cat_list = pandas.get_dummies(df[var], prefix=var)
    data1 = df.join(cat_list)
    df = data1

cat_vars = list_cat_vars
data_vars = df.columns.values.tolist()
to_keep = [i for i in data_vars if i not in cat_vars]
data_final = df[to_keep]
print(len(data_final.columns.values))

#data_final.to_csv(f"{path}data_lr5")

X = data_final.loc[:, data_final.columns != 'MCQ010']
y = data_final.loc[:, data_final.columns == 'MCQ010']

os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns

os_data_X, os_data_y = os.fit_resample(X_train, y_train)
os_data_X = pandas.DataFrame(data=os_data_X, columns=columns )
os_data_y = pandas.DataFrame(data=os_data_y, columns=['MCQ010'])

# we can Check the numbers of our data
print("length of oversampled data is ", len(os_data_X))
print("Number of no subscription in oversampled data", len(os_data_y[os_data_y['MCQ010'] == 0]))
print("Number of subscription", len(os_data_y[os_data_y['MCQ010']==1]))
print("Proportion of no subscription data in oversampled data is ", len(os_data_y[os_data_y['MCQ010']==0]) / len(os_data_X))
print("Proportion of subscription data in oversampled data is ", len(os_data_y[os_data_y['MCQ010']==1]) / len(os_data_X))

data_final_vars = data_final.columns.values.tolist()
y = ['MCQ010']
X = [i for i in data_final_vars if i not in y]

logreg = LogisticRegression(max_iter=1000)
rfe = RFE(logreg, 20)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)