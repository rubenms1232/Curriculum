import os
import pandas as pd

# Path of the file you want to enumerate
path = "/home/xxx/Documentos/xxx/output"
directory = []
filename = []

for (root, dirs, files) in os.walk(path):
    for f in files:
        directory.append(root)
        filename.append(f)
        print(f)

# Column names of the dataframe
df = pd.DataFrame(list(zip(directory, filename)), columns=['Directory', "Filename"])

# Change the format of the exported file to CSV
df.to_csv("xxx.csv", index=False)
