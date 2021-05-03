# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import openpyxl
import os

path = 'csv_datasets/'
dataframe_name = "df_valid"
new_path = 'datasets/'
dataframe_name_allergy = "df_allergy"
filenames = []
column_name = ['SEQN', 'AGQ010_x', 'AGQ040_x', 'AGQ070_x', 'AGQ090_x', 'AGQ100_x', 'AGQ120_x', 'AGQ130_x',
               'AGQ180_x', 'Allergy_Seasons_x', 'AUQ131', 'BPQ020', 'HSQ500', 'HSQ510', 'HSQ520',
               'HSD010', 'HSQ470', 'HSQ480', 'HSQ490', 'RIAGENDR', 'RIDAGEYR',
                'RIDRETH1', 'DMQMILIT', 'DMDBORN', 'DMDCITZN', 'DMDMARTL', 'DMDHHSIZ',
               'INDHHINC', 'INDFMINC', 'INDFMPIR', 'DMDHRGND', 'DMDHREDU', 'DMDHRMAR',

               'DMDFMSIZ', 'DIQ010',
               'DIQ050', 'DIQ160', 'DIQ170', 'DIQ180', 'DIQ190A', 'DIQ190B', 'DIQ190C', 'DIQ200A', 'DIQ200B',
               'DIQ200C', 'DBQ700', 'DBQ197', 'DBD091', 'DBQ720', 'DBQ730', 'DBQ740', 'DBQ750', 'DBQ760',
               'DBQ770', 'DBQ780', 'DBQ890', 'FSD170N', 'FSD180', 'FSD032A', 'FSD032B', 'FSD032C', 'FSDHH',
               'FSDAD', 'FSD151', 'FSQ170', 'FSQ162', 'HIQ210', 'HIQ011', 'HIQ270', 'HUQ010', 'HUQ020',
               'HUQ030', 'HUQ040', 'HUQ050', 'HUQ090', 'HUQ071', 'MCQ010', 'MCQ053', 'MCQ080', 'MCQ092',
               'MCQ140', 'MCQ245A', 'OCD150', 'OCD390G', 'OHQ620', 'OHQ630', 'OHQ640', 'OHQ650', 'OHQ660',
               'OHQ670', 'OHQ680', 'OHQ011', 'PUQ100', 'PUQ110', 'PAD020', 'PAQ100', 'PAQ180', 'PAD200',
               'PAD320', 'PAD440', 'PAQ500', 'PAQ520', 'PAD590', 'PAD600', 'RXDUSE',
               'RDQ070', 'RDQ140', 'SLD010H', 'SLD020M', 'SLQ030', 'SLQ040', 'SLQ050', 'SLQ060',
               'SLQ080', 'SLQ090', 'SLQ100', 'SLQ110', 'SLQ120', 'SLQ130', 'SLQ140', 'SLQ150', 'SLQ160', 'SLQ170',
               'SLQ180', 'SLQ190', 'SLQ200', 'SLQ210', 'SLQ220', 'SLQ230', 'SLQ240', 'SMDUPCA',
                'SMD410', 'SMQ680', 'WHD010', 'WHD020', 'WHQ030', 'WHD050', 'WHQ070',
               'WHD140', 'WHQ040', 'WHQ150']

df = pandas.read_csv(f"{path}{dataframe_name}", low_memory=False)
new_data = df[df.columns.intersection(column_name)]
new_data.to_csv(f"{path}data_valid_25")
print(new_data)

