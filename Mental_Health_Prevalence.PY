import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
from PIL import Image
import statistics
prevalence_df = pd.read_csv(r'C:\Users\USER\Downloads\prevalence-by-mental-and-substance-use-disorder.csv')
print(prevalence_df)
#get a general info
print(prevalence_df.info())
#get column names
print(prevalence_df.columns)
#what are the components of Entity, Code columns and then both
print(prevalence_df['Entity'])
print(prevalence_df['Code'])
print(prevalence_df[['Entity','Code']])
#to check if Ghana is in the set
print(prevalence_df[prevalence_df.Entity== 'Ghana'])
#to check if Ghana is in the set
print(prevalence_df[prevalence_df.Entity== 'Nigeria'])
#what is data can be found at column 5000
print(prevalence_df.loc[5000])
#what is the value at column 4000 for Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)
print(prevalence_df.at[4000,'Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)'])
#extract data for Ghana
Ghana_prevalence_df = prevalence_df[prevalence_df.Entity== 'Ghana']
print(Ghana_prevalence_df)
#extract data for Nigeria
Nigeria_prevalence_df =prevalence_df[prevalence_df.Entity== 'Nigeria']
print(Nigeria_prevalence_df)
UK_prevalence_df = prevalence_df[prevalence_df.Entity== 'United Kingdom']
print(UK_prevalence_df)
#find the Sum of Nigeria depressive disorders
Nigeria_depression_disorder_sum = Nigeria_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].sum()
print(Nigeria_depression_disorder_sum)
#find the Sum of Ghana depressive disorders
Ghana_depression_disorder_sum = Ghana_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].sum()
print(Ghana_depression_disorder_sum)
#find the Sum of UK depressive disorders
UK_depression_disorder_sum = UK_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].sum()
print(UK_depression_disorder_sum)
#find the mean of UK depressive disorders
UK_depression_disorder_mean = UK_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].mean()
print(UK_depression_disorder_mean)
#find the mean of Ghana depressive disorders
Ghana_depression_disorder_mean = Ghana_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].mean()
print(Ghana_depression_disorder_mean)
#find the mean of Nigeria depressive disorders
Nigeria_depression_disorder_mean = Nigeria_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].mean()
print(Nigeria_depression_disorder_mean)
#create a bar chat to represent the means
mean_df = [UK_depression_disorder_mean,Ghana_depression_disorder_mean,Nigeria_depression_disorder_mean]
country = ['UK','GH','NGN']
plt.bar(country,mean_df)
plt.show()
#find the cumulative some of depressive disorders in the 3 entities
Nigeria_depression_disorder_cum_sum = Nigeria_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].cumsum()
print(Nigeria_depression_disorder_cum_sum)
Ghana_depression_disorder_cum_sum = Ghana_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].cumsum()
print(Ghana_depression_disorder_cum_sum)
UK_depression_disorder_cum_sum = UK_prevalence_df['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].cumsum()
print(UK_depression_disorder_cum_sum)
#sort the depressive disorders in the 3 entities in descending order to display first 10
Nigeria_depression_disorder_sorted = Nigeria_prevalence_df.sort_values('Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False).head(10)
print(Nigeria_depression_disorder_sorted)                                                  
Ghana_depression_disorder_sorted = Ghana_prevalence_df.sort_values('Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False).head(10)
print(Ghana_depression_disorder_sorted)
UK_depression_disorder_sorted = UK_prevalence_df.sort_values('Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False).head(10)
print(UK_depression_disorder_sorted)
#find the sum of depressive disorder for each country in the dataset
depressive_disorder_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(depressive_disorder_sum_by_country)
#sort out to find country with highest and lowest disorder
sorted_depressive_disorder_sum_by_country= depressive_disorder_sum_by_country.sort_values('Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_depressive_disorder_sum_by_country)
#create a plot
sns.barplot(data=depressive_disorder_sum_by_country,x='Entity',y='Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)')
plt.show()
#find the sum of 3 categories for each entity
overview_three_categories = prevalence_df.groupby('Entity')[['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)','Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)','Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(overview_three_categories)
#find the total for each entity for schizophrenia
schizophrenia_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(schizophrenia_sum_by_country)
#sortout the entities in descending order based o schizophrenia
sorted_schizophrenia = schizophrenia_sum_by_country.sort_values('Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)',ascending= False)
print(sorted_schizophrenia)
#draw a scatter plot for total of schizophrenia based on entities
sns.scatterplot(data= schizophrenia_sum_by_country,x='Entity',y='Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('Schizophrenia distribution based on country')
plt.show()
#find the total for each entity for bipolar
bipolar_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(bipolar_sum_by_country)
#sortout the entities in descending order based on bipolar
sorted_bipolar_sum_by_country = bipolar_sum_by_country.sort_values('Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)', ascending= False)
print(sorted_bipolar_sum_by_country)
#draw a sctter plot for total of bipolar based on entities
sns.scatterplot(data=bipolar_sum_by_country, x='Entity',y='Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('Bipolar distribution based on country')
plt.show()
#find the total for each entity for eating disorder
eating_disorder_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(eating_disorder_sum_by_country)
#sortout the entities in descending order based on eating disorder
sorted_eating_disorder_sum_by_country = eating_disorder_sum_by_country.sort_values('Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_eating_disorder_sum_by_country)
#draw a scatter plot for total of eating disorder based on entities
sns.scatterplot(data=eating_disorder_sum_by_country,x='Entity',y='Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('Eating disorder distribution based on country')
plt.show()
#find the total for each entity for anxiety disorder
anxiety_disorder_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(anxiety_disorder_sum_by_country)
#sortout the entities in descending order based on anxiety disorder
sorted_anxiety_disorder_sum_by_country = anxiety_disorder_sum_by_country.sort_values('Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_anxiety_disorder_sum_by_country)
#draw a scatter plot for total of anxiety disorder based on entities
sns.scatterplot(data=anxiety_disorder_sum_by_country,x='Entity',y='Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('anxiety disorder distribution based on country')
#find the total for each entity for drug use disorder
drug_use_disorder_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(drug_use_disorder_sum_by_country)
#sortout the entities in descending order based on drug use disorder
sorted_drug_use_disorder_sum_by_country = drug_use_disorder_sum_by_country.sort_values('Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_drug_use_disorder_sum_by_country)
#draw a scatter plot for total of drug use disorder based on entities
sns.scatterplot(data=drug_use_disorder_sum_by_country,x='Entity',y='Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('drug use disorder distribution based on country')
plt.show()
#find the total for each entity for alcohol use disorder
Alcohol_use_disorder_sum_by_country = prevalence_df.groupby('Entity')[['Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(Alcohol_use_disorder_sum_by_country)
#sortout the entities in descending order based on alcohol use disorder
sorted_Alcohol_use_disorder_sum_by_country = Alcohol_use_disorder_sum_by_country.sort_values('Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_Alcohol_use_disorder_sum_by_country)
#draw a scatter plot for total of alcohol use disorder based on entities
sns.scatterplot(data=Alcohol_use_disorder_sum_by_country,x='Entity',y='Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Entity')
plt.title('Alcohol use disorder distribution based on country')
plt.show()
#find the total for each year based on depressive disorder
depressive_disorder_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(depressive_disorder_sum_by_year)
#sortout the years in descending order based on depressive disorder
sorted_depressive_disorder_sum_by_year = depressive_disorder_sum_by_year.sort_values('Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)')
print(sorted_depressive_disorder_sum_by_year)
#draw a scatter plot for total of depressive disorder based on year
sns.scatterplot(data=depressive_disorder_sum_by_year,x='Year',y='Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('Depressive disorder distribution by Year')
plt.show()
#find the total for each  year based on schizophrenia disorderr
schizophrenia_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)']].sum()
#sortout the years in descending order based on schizophrenia disorder
sorted_schizophrenia_sum_by_year = schizophrenia_sum_by_year.sort_values('Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_schizophrenia_sum_by_year)
#draw a scatter plot for total of schizophrenia disorder based on year
sns.scatterplot(data=schizophrenia_sum_by_year, x='Year',y='Prevalence - Schizophrenia - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('schizophrenia distribution by year')
plt.show()
#find the total for each  year based on bipolar disorder
bipolar_disorder_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(bipolar_disorder_sum_by_year)
sorted_bipolar_disorder_sum_by_year = bipolar_disorder_sum_by_year.sort_values('Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)',ascending = False)
print(sorted_bipolar_disorder_sum_by_year)
sns.scatterplot(data=bipolar_disorder_sum_by_year,x='Year',y='Prevalence - Bipolar disorder - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('bipolar distribution by year')
plt.show()
eating_disorder_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(eating_disorder_sum_by_year)
#sortout the years in descending order based on eating disorder
sorted_eating_disorder_sum_by_year = eating_disorder_sum_by_year.sort_values('Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_eating_disorder_sum_by_year)
#draw a scatter plot for total of eating disorder based on year
sns.scatterplot(data=eating_disorder_sum_by_year,x='Year',y='Prevalence - Eating disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('Eating disorder distribution by year')
plt.show()
#find the total for each year for anxiety disorder
anxiety_disorder_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(anxiety_disorder_sum_by_year)
#sortout the years in descending order based on anxiety disorder
sorted_anxiety_disorder_sum_by_year = anxiety_disorder_sum_by_year.sort_values('Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_anxiety_disorder_sum_by_year)
#draw a scatter plot for total of anxiety disorder based on year
sns.scatterplot(data=anxiety_disorder_sum_by_year,x='Year',y='Prevalence - Anxiety disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('anxiety disorder distribution by Year')
#find the total for each year for drug use disorder
drug_use_disorder_sum_by_year = prevalence_df.groupby('Year')[['Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(drug_use_disorder_sum_by_year)
#sortout the years in descending order based on drug use disorder
sorted_drug_use_disorder_sum_by_year = drug_use_disorder_sum_by_year.sort_values('Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_drug_use_disorder_sum_by_year)
#draw a scatter plot for total of drug use disorder based on years
sns.scatterplot(data=drug_use_disorder_sum_by_year,x='Year',y='Prevalence - Drug use disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('drug use disorder distribution by Year')
plt.show()
#find the total for each year for alcohol use disorder
Alcohol_use_disorder_sum_by_year= prevalence_df.groupby('Year')[['Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)']].sum()
print(Alcohol_use_disorder_sum_by_year)
#sortout the years in descending order based on alcohol use disorder
sorted_Alcohol_use_disorder_sum_by_year = Alcohol_use_disorder_sum_by_year.sort_values('Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)',ascending=False)
print(sorted_Alcohol_use_disorder_sum_by_year)
#draw a scatter plot for total of alcohol use disorder based on years
sns.scatterplot(data=Alcohol_use_disorder_sum_by_year,x='Year',y='Prevalence - Alcohol use disorders - Sex: Both - Age: Age-standardized (Percent)',hue='Year')
plt.title('Alcohol use disorder distribution by Year')
plt.show()