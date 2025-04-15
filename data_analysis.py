import pandas as pd
import matplotlib.pyplot as plt

def analyze():
    try:
        grades = pd.read_csv("grades.txt", names=['ID', 'Math', 'Science', 'English', 'Social Studies', 'Computer'])
        eca = pd.read_csv("eca.txt", names=['ID', 'Activities'])

# Plotting bar graph for average grades in every subject
        avg= grades.iloc[:, 1:].mean()
        print("Average Grades:")
        print(avg)
        avg.plot(kind='bar',title='Average Grades in every Subject')
        plt.show()

# Comparing academic performance and ECA participation of every student
        eca['ECA Count'] = eca['Activities'].apply(lambda x: len(x.split(';')))
        merged = pd.merge(grades, eca[['ID', 'ECA Count']], on='ID', how='left')
        merged['Average Grade'] = merged.iloc[:, 1:6].mean(axis=1)

        plt.scatter(merged['ECA Count'], merged['Average Grade'])
        plt.title('ECA Participation vs Academic Performance')
        plt.xlabel('Number of ECAs')
        plt.ylabel('Average Grade')
        plt.show()

    except Exception as e:
        print("Error analyzing data:", e)
