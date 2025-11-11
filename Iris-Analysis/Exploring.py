import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset

df = pd.read_csv("./Iris.csv")
print("FIRST 5 ROWS:")
print(df.head())  

species_df = {}
for species in df['species'].unique():
    species_data = df[df['species'] == species]
    print(f"\n Species: {species}")
    print(species_data.describe()) # Summary statistics for each species
    species_df[species] = species_data

print(species_df['virginica'])

# Missing values
Missing_values = df.isnull().sum()
print("\nMISSING VALUES:")
print(Missing_values)


# Correlation matrix using only numeric columns
corr = df.corr(numeric_only=True)
print("Correlation Matrix:\n", corr)


# Heatmap of the correlation matrix

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


#Pait plot
sns.pairplot(df, hue='species')
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

  # Data types of each column


print("\nSUMMARY:")
print(df.describe())  # Summary statistics of the datase




#did some more experimets


sns.boxplot(x='species', y='sepal_length', data=df)
plt.title("Boxplot of Sepal Length by Species")

plt.show() #plot boxplot



 # Data types of each column

# Violin plots for each feature by species
for col in df.columns[:-1]:
    sns.violinplot(x='species', y=col, data=df)
    plt.title(f"{col} Distribution by Species")
    plt.show()
