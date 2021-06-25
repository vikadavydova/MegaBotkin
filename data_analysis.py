# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas
import mimetypes
import pyreadstat
import os
import xport


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# here begins my code section

#here lies section to change
path = 'datasets/Mental Health - Depression/'
dataframe_name = "df_mental_health_depression"

path_a = "CIQDEP_B.XPT"
path_b = "CIQDEP_C.XPT"
path_c = "CIQMDEP.XPT"
#path_d = "DPQ_G.XPT"
#path_e = "DPQ_H.XPT"
#path_f = "DPQ_I.XPT"
#path_g = "DPQ_J.XPT"
#path_h = "DEMO_H.XPT"
#path_i = "DEMO_I.XPT"
#path_j = "DEMO_J.XPT"

df_a = pandas.read_sas(f"{path}{path_a}")
df_b = pandas.read_sas(f"{path}{path_b}")
df_c = pandas.read_sas(f"{path}{path_c}")
#df_d = pandas.read_sas(f"{path}{path_d}")
#df_e = pandas.read_sas(f"{path}{path_e}")
#df_f = pandas.read_sas(f"{path}{path_f}")
#df_g = pandas.read_sas(f"{path}{path_g}")
#df_h = pandas.read_sas(f"{path}{path_h}")
#df_i = pandas.read_sas(f"{path}{path_i}")
#df_j = pandas.read_sas(f"{path}{path_j}")


#here ends section to change


#df_mcq_j_1718 = pandas.read_sas('datasets/mcq_j_1718.xpt')
#new_df = df_cdq_1718.merge(df_mcq_j_1718, left_on='SEQN', right_on='SEQN', how='inner', suffixes=('_left', '_right'))

df_sum = pandas.concat([
    df_a,
    df_b,
    df_c
#    df_d,
#    df_e,
#    df_f,
#    df_g
#    df_h,
 #   df_i,
 #   df_j
], ignore_index=True)

#df_sum = pandas.concat([df_a, df_b, df_c],  ignore_index=True)

#pyreadstat.write_xport(df_cdq_9918, "CDQ_9918.XPT")
#df_cdq_9918.to_pickle("./dummy.pkl")
#print(mimetypes.guess_type('datasets/CDQ_9918.XPT'))
#new_pickle = pandas.read_pickle("./dummy.pkl")


print(df_a)
print(df_sum)
df_sum.to_csv(f"./csv_datasets/{dataframe_name}")
print(df_sum.isna().sum())

#here we can concatenate the columns
#df_sum['ACD011A'].fillna(df_sum['ACD010A'], inplace=True)
#del df_sum['ACD010A']
#print(df_sum)


#print(df_cdq_9918.isna().sum())
#print(check_df.isna().sum())
# print(df_cdq_1718)
# print(df_mcq_j_1718)


#df_card = pandas.read_pickle("pickle/df_cardiovascular_health")
#print(df_card)
#print(len(df_card) - df_card.count())