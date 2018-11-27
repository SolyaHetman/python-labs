import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

def task1():
    data= pd.read_csv('NYC_Jobs.csv', sep=',')
    print (data)

def task2():
    data = pd.read_csv('NYC_Jobs.csv')
    print(data[:10])
    print(data['Agency'][:10])
    print(data[['Agency','Work Location 1','Business Title']][:3])


def task3():
    data = pd.read_csv('NYC_Jobs.csv')
    data_counts = data['Agency'].value_counts()
    data_counts[:30].plot(kind='bar')
    plt.show()


def task4():
    data = pd.read_csv('NYC_Jobs.csv')
    data['median'] = data.groupby('Salary Range From')['Salary Range To'].transform(np.median)
    gb = data.groupby('Agency')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1[:30].plot(kind='bar')
    plt.show()

    gb = data.groupby('Work Location')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1[:30].plot(kind='bar')
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('NYC_Jobs.csv')
    n = 1

    print(' 1 = task 1'
          ' 2 = task 2'
          ' 3 = task 3'
          ' 4 = task 4'
          ' 0 = to exit')
    while (n != 0):
        n = int(input())
        if (n == 1):
             task1()
        elif (n == 2):
            task2()
        elif (n == 3):
            task3()
        elif (n == 4):
            task4()