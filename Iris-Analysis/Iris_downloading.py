import pandas as pd
import seaborn as sns

df = sns.load_dataset('Iris') # Load the Iris dataset using seaborn
df.to_csv('Iris.csv', index=False) # Save the dataset as a CSV file without the index using pandas
print("Iris dataset has been downloaded and saved as 'Iris.csv'.")  


