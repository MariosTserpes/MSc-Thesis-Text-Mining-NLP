import pandas as pd 
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
