import pandas as pd 

import plotly.express as px #pip install plotly
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.style.use('ggplot')


fake_news = pd.read_csv('Fake.csv')
real_news = pd.read_csv('True.csv')

for data in [fake_news, real_news]:
    print(data.shape)
    
# Create Target based on Real and Fake data
real_news['Category'] = 'Real_News'
fake_news['Category'] = 'Fake_News'

dataset = pd.concat([real_news, fake_news]).reset_index(drop=True)
print(dataset.shape)
print(dataset.isnull().sum())

def plot_data(column, plot_title, input_xlabel):
    fig4, ax4 =  plt.subplots(1,1, figsize=(10, 6))
    array = dataset[column].value_counts().sort_values(ascending = False)
    ax4.bar(array.index, array, width = 0.7, edgecolor = 'black', color = 'purple',  linewidth = 0.1, alpha = 0.4)
    for i in array.index:
        ax4.annotate(f"{array[i]}",  xy=(i, array[i] + 120),
                        va = 'center', ha='center',fontweight='light', 
                        color='black', fontsize = 13)
    ax4.set_title(plot_title, fontsize = 20)
    ax4.set(ylabel = 'Count_News', xlabel = input_xlabel)
    plt.xticks(rotation = 45, fontweight = 'bold')
    
plot_data('subject', 'Number of News', 'Subject')
plot_data('Category', 'Number of Fake and Real News', 'Category')



#A function which visualize lenght of corpora, passing as parameter the name of column as string
def plot_length(input_variable):
    fig = px.histogram(dataset, 
                   x = dataset[input_variable].astype(str).apply(len),
                   color="Category")
    fig.show()
    
plot_length('text')    
plot_length('title')


def boxplots(input_variable):
    fig = px.box(dataset,  
                 x = "Category", 
                 y = dataset[input_variable].astype(str).apply(len))
    fig.show()
    
boxplots('text')
boxplots('title')


#A function in order to calculate the number for each statement
def plot_word_count(input_variable):
    fig = px.histogram(dataset,
                       x = dataset[input_variable].apply(lambda x: len(str(x).split())), 
                       color = 'Category')
    fig.show()
    
plot_word_count('text')
plot_word_count('title')


#Descriptive Statistics for word_count
def descriptine_statistics_word_count(input_variable, news_category):
    #1. input_variable : Input 'text' or 'title'
    #2. news_category  : Input 'Fake_News' or 'Real_News'
    subset = dataset[dataset['Category'] == news_category]
    descriptive_stats = subset[input_variable].apply(lambda x: len(str(x).split())).describe()
    print(f'Descrptive Statistics for {input_variable} variable and {news_category} category:\n {descriptive_stats}')
  
# For text
descriptine_statistics_word_count('text', 'Fake_News')
descriptine_statistics_word_count('text', 'Real_News')

#For title
descriptine_statistics_word_count('title', 'Fake_News')
descriptine_statistics_word_count('title', 'Real_News')

#The merged_set.csv will be utilized for generating wordclouds and cleansing data
#dataset.to_csv('merged_set.csv')
