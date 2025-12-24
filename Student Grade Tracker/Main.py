import pandas as pd
import numpy as np
import os

DATA_FILE = "students.csv"

# Ensure CSV exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Grade"])
    df.to_csv(DATA_FILE, index=False)

# Heelper Functions 

def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def clean_data(df):
    # Strip whitspace from names
    df['Name'] = df['Name'].str.strip()
    
    # Convert grads to numeric, coerce errors 
    df['Grade'] = pd.to_numeric(df['Grade'], errors='coerce')
    
    # Remove invalid grades (NaN or outside 0-100)
    df = df[df['Grade'].between(0, 100)]
    
    df.reset_index(drop=True, inplace=True)
    return df

def add_student():
    name = input("Enter student name: ").strip()
    grade = input("Enter grade (0-100): ").strip()
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            raise ValueError
    except:
        print("Invalid grade!")
        return
    
    df = load_data()
    df = df.append({"Name": name, "Grade": grade}, ignore_index=True)
    save_data(df)
    print(f"Added {name} with grade {grade}")

def view_students():
    df = load_data()
    df = clean_data(df)
    if df.empty:
        print("No valid student data.")
        return
    
    print("\nStudent Grades:")
    print(df.to_string(index=False))
    
    print("\nStatistics:")
    print(f"Average Grade: {df['Grade'].mean():.2f}")
    print(f"Highest Grade: {df['Grade'].max()}")
    print(f"Lowest Grade: {df['Grade'].min()}")

# 

def main():
    while True:
        print("\nStudent Grade Tracker (pandas + NumPy)")
        print("1. View Students")
        print("2. Add Student")
        print("3. Clean Data")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            view_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            df = load_data()
            df = clean_data(df)
            save_data(df)
            print("Data cleaned successfully!")
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

