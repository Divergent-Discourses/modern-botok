import os
import pandas as pd

# File path
home_dir = os.getcwd()
file_path = home_dir + "/dictionary/custom/dictionary/words/tsikchen.tsv"
dict_path = '/home/yuki/Dropbox/Arbeit/20240112_Divergierende_Diskurse/20240216_POS-Tagger/api/AcTib/dictionary/'

# Read the tab-separated table
table = pd.read_csv(file_path, sep='\t', dtype='str')[1:]
table['freq'] = table['freq'].fillna(pd.NA).astype(pd.Int64Dtype())

# check if there are words that have more than four syllables and remove them
forms = []
for form in table['# form']:
    syllables = form.split('་')
    if len(syllables) < 5:
        forms.append(form)
new_table = table[table['# form'].isin(forms)]

# export the new table
file_name = dict_path + 'tsikchen_new.tsv'
new_table.to_csv(file_name, sep='\t', index=False)