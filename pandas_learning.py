# Part 1: Data Loading and Inspection
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students_data - students_data.csv') # Load the dataset into a Pandas DataFrame.
print(df.head(100)) # Display the first 10 rows of the DataFrame. 
df.info() # Data types of columns
print(df.shape) # Shape of the DataFrame
print(df.describe()) # Basic statistics using .describe()
print(df.isnull().values.any()) #To check if there any missing values
print(df.isnull().sum().sum()) #To know how many null values

# Part 2: Data Cleaning
df['Grade'] = df['Grade'].fillna(df['Grade'].mean()) # Replace missing Grade values with the column's mean
print(df['Grade'].isnull().sum().sum()) # checks this worked, should say 0
df['Attendance'] = df['Attendance'].fillna(0) # Fill missing Attendance values with a constant value (e.g., 0). 
print(df['Attendance'].isnull().sum()) # checks this worked, should say 0
df = df.dropna(subset=['Name', 'StudentID'])
print(df['Name'].isnull().sum()) # checks this worked, should say 0
print(df['StudentID'].isnull().sum())
df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female', 'male': 'Male', 'female': 'Female'}) # Standardize the Gender column to ensure values are consistent (e.g., replace "M" with "Male" and "F" with "Female").

# Part 3: Data Manipulation
def pass_fail(x):   # Add a new column called Pass/Fail:
                    # A student passes if their Grade is 50 or above.
    if x > 50:
        return 'Pass'
    else:
        return 'Fail'
    
df['Pass/Fail'] = df['Grade'].apply(pass_fail)
print(df['Pass/Fail']) # checks if this worked

high_attendance_df = df[df['Attendance'] > 75] # Creates a new DataFrame for students with Attendance > 75%
high_attendance_df = high_attendance_df.sort_values(by='Attendance', ascending=False) # Sort the DataFrame by Grade in descending order

# Part 4: Data Analysis
print(df.groupby('Subject')['Grade'].mean()) # Group the data by Subject and calculate the average Grade for each subject. 
print(df.groupby('Subject', group_keys=False).apply(lambda g: g.nlargest(3, 'Grade'))) # Find the top 3 students with the highest grades in each subject.
pivot_table = pd.pivot_table(df, values='Grade', index='Subject', columns='Gender', aggfunc='mean') # Create a pivot table showing the average Grade of students for each Subject and Gender.
print(pivot_table)

# Part 5: Visualization
# A bar chart of the average grades per subject.

avg_grades = df.groupby('Subject')['Grade'].mean()

avg_grades.plot(kind='bar', title='Average Grade per Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.tight_layout()
plt.show()

# A pie chart showing the proportion of males and females in the dataset.
gender_counts = df['Gender'].value_counts()

gender_counts.plot(kind='pie', autopct='%1.1f%%', title='Gender Distribution')
plt.ylabel('')  # Optional: hides the default y-axis label
plt.tight_layout()
plt.show()

# A scatter plot of Grade vs. Attendance.

df.plot(kind='scatter', x='Attendance', y='Grade', title='Grade vs. Attendance')
plt.tight_layout()
plt.show()