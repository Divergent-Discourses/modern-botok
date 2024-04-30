import os
import pandas as pd
import pyewts

# File path
home_dir = os.getcwd()
file_path = home_dir + "/your/path/tsikchen.tsv"
dict_path = '/your/path/dictionary/'
dict_file = 'dictionary_name.txt'
dict_file_path = dict_path + dict_file

# Read the tab-separated table
table = pd.read_csv(file_path, sep='\t', dtype='str')[1:]
dictionary = pd.read_csv(dict_file_path, header=None, names=['word'])
table['freq'] = table['freq'].fillna(pd.NA).astype(pd.Int64Dtype())

# Convert Wylie to Tibetan script
converter = pyewts.pyewts()
converted_list = []
for index, value in dictionary.iterrows():
    wylie = str(value.iloc[0])
    converted = converter.toUnicode(wylie)
    if converted not in table['# form'].values:
        converted_list.append(converted)

# concatenate the converted_list with the table
new_words = pd.DataFrame({'# form': converted_list})
for col in table.columns[1:]:
    new_words[col] = ''
new_table = pd.concat([table, new_words], ignore_index=True)

# export the new table
base_dir = os.path.dirname(dict_path)
file_name = dict_path + 'tsikchen_new.tsv'
new_table.to_csv(file_name, sep='\t', index=False)