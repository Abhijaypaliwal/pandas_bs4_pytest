import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [21, 22, 23],
    'City': ['NY', 'Paris', 'London']
}

print(type(data['Name']))
print(data['Name'][0:3])

data_students = pd.read_csv('StudentData.csv')
#show top 5 data
print(data_students.head())
#give info about all the dtypes
print(data_students.info())

#give measure of central tendency(statistical data)
print(data_students.describe())
#get null field values
print(data_students.isnull().sum())
#remove blank values
data_students = data_students.dropna()
print(data_students.isnull().sum())
#to count the values
print(data_students.gender.value_counts())

#plt.bar( ['male', 'female'], data_students.gender.value_counts(), align='center')


# plt.title('Gender counts')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.plot()
# plt.show()

# avg_marks = data_students.groupby('course')['marks'].mean()
#
# avg_marks.plot(kind='bar', title='Average Marks')
# plt.show()
sort_values = data_students.sort_values(by=['marks'], ascending=False)
print(sort_values[['name', 'course', 'marks']].head(10) )

data_students['result'] = data_students.apply(lambda x: "Pass" if x['marks'] > 50 else "Fail", axis=1)



print(data_students.head(10))

print((data_students['result']=='Pass').mean())




