import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset

df = pd.read_csv("./Iris.csv")
print("FIRST 5 ROWS:")
print(df.head())  

for col in df.columns[:-1]:  # Exclude the species column (loop iterates 4 times)
    sns.violinplot(x='species', y=col, data=df)
    plt.title(f"{col} Distribution by Species")
    plt.xlabel("Species")
    plt.show()
