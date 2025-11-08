import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("iris.csv")

print("FIRST 5 ROWS:")
print(df.head())

print("\nSUMMARY:")
print(df.describe())

# Pairplot
sns.pairplot(df, hue="species")
plt.show()

# Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True)
plt.show()

plt.scatter(df['sepal_length'], df['petal_length'])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()


