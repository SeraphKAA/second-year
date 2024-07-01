import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class pandas_sas:
    def __init__(self, df):
        self.df = df

    def zad_1(self):
        self.df.columns = self.df.columns.str.replace('Time/months', 'Time')
        self.df.loc[self.df["whether he/he donated blood"] == 1, "whether he/he donated blood"] = 'Yes'
        self.df.loc[self.df["whether he/he donated blood"] == 0, "whether he/he donated blood"] = 'Noup'
        return self.df

    def zad_2(self):
        self.zad_1()
        self.df['Test'] = self.df[['Recency (months)', 'Frequency (times)']].sum(axis=1)
        return self.df
    
    
    def zad_3(self):
        return self.df.describe()
    
    def zad_4(self):
        a = self.df.groupby('Recency (months)').mean()
        print(a, '\n', a.sum())
        aa = self.df.sort_values(['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time'], ascending = True)
        bb = self.df.sort_values(['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time'], ascending = False)
        print(aa, '\n', bb)
        self.df = self.df.select_dtypes(include = np.number)
        self.df.mean()
        self.df.hist()
        plt.show()

    
    def zad_5(self):
        self.df = self.df[self.df['Time'] > self.df['Time'].mean()]
        self.df[['Time']] = df[['Time']].astype(float)
        print(self.df['Recency (months)'].value_counts())
        print(self.df['Frequency (times)'].value_counts())
        print(self.df['Monetary (c.c. blood)'].value_counts())
        print(self.df['Time'].value_counts())
        print(self.df['Test'].value_counts())
        
    
    def zad_6(self):
        dd = self.df[self.df['Frequency (times)'] > self.df['Frequency (times)'].mean()]
        ass = self.df.groupby('Recency (months)')
        ass = dd.select_dtypes(include = np.number)
        ass.hist()
        plt.show()
    
    
    def zad_7(self):
        self.df = self.df.query('Time > 2').groupby('Recency (months)')['Time']
        self.df.mean().plot(kind = 'bar', sharex = True, sharey = True, color = 'lightblue')
        self.df.min().plot(kind = 'bar')
        plt.show()




def vizov():
    print(A.zad_1())        #+
    print(A.zad_2())        #+
    a = '-' * 100
    print(a)
    print(A.zad_3())        #+
    print(A.zad_4())        #+
    print(A.zad_5())        #+
    print(A.zad_6())        #+
    print(A.zad_7())        #+

if __name__ == '__main__':
    df = pd.DataFrame(pd.read_excel('C:\\Users\\79045\\Desktop\\бессоные ночи\\сделанное дз\\2 курс 3 сем\\ОП\\pandas sas\\test.xlsx'))
    A = pandas_sas(df)
    vizov()

















'''
def sda():
#Задание 1

    df = pd.DataFrame(pd.read_excel('test.xlsx')) #        'text mini.xlsx'          'test.xlsx'           'laba 4 pandas1.xlsx'
    df.columns = df.columns.str.replace('Time/months', 'Time')
    # df.columns = df.columns.str.replace('BMI', 'BMX (BMI)')               #for laba 4 pandas1
    df.loc[df["whether he or she donated blood"] == 1, "whether he or she donated blood"] = 'Yes'
    df.loc[df["whether he or she donated blood"] == 0, "whether he or she donated blood"] = 'Noup'
    # df[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time/months', 'whether he or she donated blood']] = df[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time/months', 'whether he or she donated blood', 'Test']].astype(float)
    print(df)
    abc = ['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time', 'whether he or she donated blood']

#Задание 2

    df['Test'] = df[['Recency (months)', 'Frequency (times)']].sum(axis=1)
    print(df)

#Задание 3

    print(df.describe())

#Задание 4

    a = df.groupby('Recency (months)').mean()
    print(a, '\n', a.sum())
    aa = df.sort_values(['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time'], ascending = True)
    bb = df.sort_values(['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time'], ascending = False)
    print(aa, '\n', bb)
    df = df.select_dtypes(include = np.number)
    df.mean()
    df.hist()
    plt.show()

#Задание 5

    # df[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time', 'Test']] = df[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time', 'Test']].astype(float)
    df = df[df['Time'] > df['Time'].mean()]
    # print(df['Recency (months)'].value_counts())
    # print(df['Frequency (times)'].value_counts())
    # print(df['Monetary (c.c. blood)'].value_counts())
    # print(df['Time)'].value_counts())
    # print(df['Test'].value_counts())

#Задание 6
    
    df = df[df['Time'] > df['Time'].mean()]
    ass = df.select_dtypes(include=np.number)
    ass.hist()
    plt.show()


# #Задание 7

'''