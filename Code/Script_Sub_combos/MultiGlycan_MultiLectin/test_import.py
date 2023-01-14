import pandas as pd
filepath = R"C:\Users\Hotsauce141\Downloads\import.txt"
glycan_file = pd.read_csv(filepath, header = None)
glycan_list = glycan_file.values.tolist()
print(glycan_list)