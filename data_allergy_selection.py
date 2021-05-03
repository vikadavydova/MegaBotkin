import pandas
import openpyxl
import os

path = 'csv_datasets/'
dataframe_name = "df_valid"
new_path = 'datasets/'
dataframe_name_allergy = "df_allergy"
filenames = []

#merge result and allergies
#df_result = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
#df_allergy = pandas.read_csv(f"{path}{dataframe_name_allergy}", low_memory=False)
#df_result = df_allergy.merge(df_result, on=['SEQN'])
#df_result_without_duplicates = df_result.drop_duplicates()
#df_result_without_duplicates.to_csv(f"./csv_datasets/df_result_with_allergy")
#print(df_result_without_duplicates)
#result_df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
#s = df_result.groupby('SEQN').first()
#print(result_df)
#print(s)
#s.to_csv(f"./csv_datasets/df_valid")
#print(s.isna().sum())


s = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
count_not_nan = s.isna().sum().to_frame()
count_not_nan.columns = ['a']
print(count_not_nan)
test = count_not_nan.loc[count_not_nan['a'] <= 1817]
test.to_excel("summary_new.xlsx")
print(test)
#for p, subdirs, files in os.walk(root):
#    for name in files:
#        filenames.append(name)

#print(filenames)
#filenames.remove('df_acculturation')
#print(filenames)

#result_df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
#for name in filenames:
#    current_df = pandas.read_csv(f"{path}{name}", low_memory=False)
#    result_df = result_df.merge(current_df, on=['SEQN'], how='outer')

#new_filename = "df_medical_conditions"
#current_df = pandas.read_csv(f"{path}{new_filename}")

#result_df = result_df.merge(current_df, on=['SEQN'], how='outer')
#print(result_df)

#print(result_df)
#result_df.to_csv(f"./csv_datasets/result_df")



#result_df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
#df_without_duplicaties = result_df.drop_duplicates()
#df_without_duplicaties.to_csv(f"./csv_datasets/df_result_without_duplicates")
#count_not_nan = df_without_duplicaties.isna().sum().to_frame()
#count_not_nan.columns = ['a']
#print(count_not_nan)
#test = count_not_nan.loc[count_not_nan['a'] <= 30269]
#test.to_excel("summary.xlsx")

#merge several columns
#path = 'datasets/Allergy/'
#dataframe_name = "df_allergy"
#path_a = 'AGQ_D.XPT'
#df_a = pandas.read_sas(f"{path}{path_a}")
#df_a['Allergy_Seasons'] = df_a[['AGQ110A', 'AGQ110B', 'AGQ110C', 'AGQ110D']].fillna('').sum(axis=1)
#print(df_a.isna().sum())
#df_a.to_csv(f"./csv_datasets/{dataframe_name}")


#print(result_df.loc[0,:])
#print(result_df.loc[1,:])
#df = pandas.read_pickle(f"{path}{dataframe_name}")
#print(df)
#df = pandas.read_csv(f"{path}{dataframe_name}")
#print(df)
#df.to_csv(f"./csv_datasets/{dataframe_name}")
#count_not_nan = df.isna().sum().to_frame()
#count_not_nan.columns = ['a']
#print(count_not_nan)
#test = count_not_nan.loc[count_not_nan['a'] <= 47938 / 2]
#print(test)