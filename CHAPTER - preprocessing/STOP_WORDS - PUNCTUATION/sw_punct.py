import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")

STOP_WORDS = stopwords.words('english')
print(STOP_WORDS)

fake_news_sample = fake_news[:500]
real_news_sample = real_news[:500]

text_fake = fake_news_sample['text'].values
title_fake = fake_news_sample['title'].values
text_real = real_news_sample['text'].values
title_real = real_news_sample['title'].values

#REMOVE PUNCTUATION
import re, string
def cleaning(input):
    for i in range(len(input)):
        words = input[i].split()
        filtered_list = []
        for word in words:
            pattern = re.compile('[^\u0000-\u007F]+', re.UNICODE)  #Remove all non-alphanumeric characters
        
            word = pattern.sub('', word)
            word = word.translate(str.maketrans('', '', string.punctuation))
            filtered_list.append(word)
            result = ' '.join(filtered_list)
        
        input[i] = result 

cleaning(text_fake)
cleaning(title_fake)
cleaning(text_real)
cleaning(title_real)



text_fake = pd.DataFrame(text_fake, columns = ['text_fake'])
title_fake = pd.DataFrame(title_fake, columns = ['title_fake'])

text_real = pd.DataFrame(text_real, columns = ['text_real'])
title_real = pd.DataFrame(title_real, columns = ['title_real'])


text_fake = text_fake['text_fake'].str.lower()
title_fake = title_fake['title_fake'].str.lower()

title_real = title_real['title_real'].str.lower()
text_real = text_real['text_real'].str.lower()


text_fake = pd.DataFrame(text_fake, columns = ['text_fake'])
title_fake = pd.DataFrame(title_fake, columns = ['title_fake'])

text_real = pd.DataFrame(text_real, columns = ['text_real'])
title_real = pd.DataFrame(title_real, columns = ['title_real'])


#REMOVE STOP_WORDS
text_fake = text_fake['text_fake'].apply(lambda x: ' '.join([word for word in x.split() if word not in (STOP_WORDS)]))
title_fake = title_fake['title_fake'].apply(lambda x: ' '.join([word for word in x.split() if word not in (STOP_WORDS)]))

text_real = text_real['text_real'].apply(lambda x: ' '.join([word for word in x.split() if word not in (STOP_WORDS)]))
title_real = title_real['title_real'].apply(lambda x: ' '.join([word for word in x.split() if word not in (STOP_WORDS)]))

#DATASETS AFTER CLEANSING
fake_cleaned = pd.concat([text_fake, title_fake, fake_news['Category'][:500]], axis = 1)
real_cleaned = pd.concat([text_real, title_real, real_news['Category'][:500]], axis = 1)

#Cleaned Datasets
#fake_cleaned.to_csv('fake_cleaned.csv')
#real_cleaned.to_csv('real_cleaned.csv')




import pandas as pd
from gensim.parsing.porter import PorterStemmer
import re, string



# p = PorterStemmer()

# for i in range(len(fake_cleaned['text_fake'].values)):

#     words = fake_cleaned['text_fake'].values[i].split()
#     filtered_list = []
#     for word in words:
#         pattern = re.compile('[^\u0000-\u007F]+', re.UNICODE)  #Remove all non-alphanumeric characters
#         word = pattern.sub('', word)
#         word = word.translate(str.maketrans('', '', string.punctuation))
#         filtered_list.append(word)
#         result = ' '.join(filtered_list)
        
#     fake_cleaned['text_fake'].values[i] = result      #if there is no text, use title
    
#     fake_cleaned['text_fake'].values[i] = p.stem_sentence( fake_cleaned['text_fake'].values[i])





#p = PorterStemmer()

# for i in range(len(fake_cleaned['title_fake'].values)):

#     words = fake_cleaned['title_fake'].values[i].split()
#     filtered_list = []
#     for word in words:
#         pattern = re.compile('[^\u0000-\u007F]+', re.UNICODE)  #Remove all non-alphanumeric characters
#         word = pattern.sub('', word)
#         word = word.translate(str.maketrans('', '', string.punctuation))
#         filtered_list.append(word)
#         result = ' '.join(filtered_list)
        
#     fake_cleaned['title_fake'].values[i] = result      #if there is no text, use title
    
#     fake_cleaned['title_fake'].values[i] = p.stem_sentence( fake_cleaned['title_fake'].values[i])





# p = PorterStemmer()

# for i in range(len(real_cleaned['text_real'].values)):

#     words = real_cleaned['text_real'].values[i].split()
#     filtered_list = []
#     for word in words:
#         pattern = re.compile('[^\u0000-\u007F]+', re.UNICODE)  #Remove all non-alphanumeric characters
#         word = pattern.sub('', word)
#         word = word.translate(str.maketrans('', '', string.punctuation))
#         filtered_list.append(word)
#         result = ' '.join(filtered_list)
        
#     real_cleaned['text_real'].values[i] = result      #if there is no text, use title
    
#     real_cleaned['text_real'].values[i] = p.stem_sentence( real_cleaned['text_real'].values[i])



fake_cleaned['word_count_text'] = fake_cleaned['text_fake'].apply(lambda x: len(str(x).split()))
fake_cleaned['word_count_title'] = fake_cleaned['title_fake'].apply(lambda x: len(str(x).split()))


real_cleaned['word_count_text'] = real_cleaned['text_real'].apply(lambda x: len(str(x).split()))
real_cleaned['word_count_title'] = real_cleaned['title_real'].apply(lambda x: len(str(x).split()))








