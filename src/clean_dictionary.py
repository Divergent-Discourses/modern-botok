import os

# File path
home_dir = os.getcwd()
file_path = home_dir + "/dictionary/custom/dictionary/words/tsikchen.tsv"
dict_path = 'your/path/'
dict_file = 'dictionary_name.txt'
dict_file_path = dict_path + dict_file

# remove unrelated parts in the dictionary, if necessary.
processed_dictionary = ''
with open(dict_file_path, 'r') as file:
    for line in file:
        # Split the line at the "|" character and keep the part before it
        processed_dictionary = processed_dictionary + line.split("|")[0].strip() + '\n'

# Open the file in write mode
new_dict_file = dict_path + 'new_' + dict_file
with open(new_dict_file, 'w') as file:
    # Write the string to the file
    file.write(processed_dictionary)