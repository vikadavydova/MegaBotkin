import pandas
import openpyxl
import os
import fsspec
import pathlib

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
data_final.to_csv(f"{path}data_lr5")