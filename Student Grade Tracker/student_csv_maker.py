import pandas as pd
import numpy as np

num_students = 200

names = [f"Student{i+1}" for i in range(num_students)]

grades = np.random.randint(-10, 110, size=num_students)  

df = pd.DataFrame({
    "Name": names,
    "Grade": grades
})

df.to_csv("students.csv", index=False)

print("Large students.csv file with 200 students has been created!")