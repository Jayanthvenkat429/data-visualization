# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:40:31 2018

@author: 39018
"""
#import the necessary library
import seaborn as sns

#load dataset present as part of the library
tips = sns.load_dataset('tips')
tips.head()

#Plot 1: Histogram
sns.distplot(tips['total_bill'])

#Plot 2: joint plot - scatter plot + histogram
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')

sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')

#Plot 3: Pair plot
sns.pairplot(tips)

sns.pairplot(tips,hue='sex',palette='coolwarm')

#Plot 4: kde plot
sns.kdeplot(tips['tip'])

#Plot 5: Bar plot
sns.barplot(x='sex',y='total_bill',data=tips)

#Plot 6: count plot
sns.countplot(x='sex',data=tips)

#Plot 7: Boxplot
sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')

sns.boxplot(data=tips,palette='rainbow',orient='h')

sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")

#Load flights data set
flights = sns.load_dataset('flights')

#Plot 8:Heat map
sns.heatmap(tips.corr())

sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)

pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)

