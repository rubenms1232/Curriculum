import os
import pandas as pd

# Path of the file you want to enumerate
path = "C:/Users/xxx/Documents"

# List to store the original filenames
original_filenames = []

# List to store the new filenames
new_filenames = []

# Counter for enumeration
counter = 1

# Loop through all files in the directory
for (root, dirs, files) in os.walk(path):
    for f in files:
        original_filenames.append(f)
        new_filename = 'P_' + str(counter) + os.path.splitext(f)[1]
        new_filenames.append(new_filename)
        os.rename(os.path.join(root, f), os.path.join(root, new_filename))
        counter += 1
        print(f, new_filename)

# Column names of the dataframe
df = pd.DataFrame(list(zip(original_filenames, new_filenames)), columns=['Original Filename', "New Filename"])

# Change the format of the exported file to CSV
df.to_csv("result.csv", index=False)
