                         


                         #    Assignment 01
    #   01. input the data
    #   02. clean the data 
    #   03. apply stemming and lematization 
    #   04. remove stop words 
    


import re    # deal with regex (regular expressions)
import nltk
from nltk.tokenize import word_tokenize



def preprocess_text(text):
    # Remove hashtags, numbers, and punctuation marks using regular expressions
    cleaned_text = re.sub(r'#\S+', '', text)  # Remove hashtags
    cleaned_text = re.sub(r'\d+', '', cleaned_text)  # Remove numbers
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Remove punctuation marks
    return cleaned_text



text="my name is Asim Qureshi. I am student of BSAI. Its basic work on NLP. I am intrested in AI. I am scared of mice. I don,t scared, its just for my data"


clean_Text= preprocess_text(text)
# print(clean_Text)                   #print clean text from here

token_text=word_tokenize(clean_Text)

# print(token_text)                    #print tokanized text from here



# stemming ,lematization 

from nltk.stem import SnowballStemmer

stemmer=SnowballStemmer("english")

stemmer_words=[]
for i in token_text:
    stemmer_words.append(stemmer.stem(i))

# print(stemmer_words)                   #print stemmer text from here
    

# lematization

from nltk.stem import WordNetLemmatizer

lematizer=WordNetLemmatizer()

lema_list=[]

for i in stemmer_words:
    lema_list.append(lematizer.lemmatize(i))

# print(lema_list)                        #print lematized text from here



# stop words remover 

from nltk.corpus import stopwords

stop=list(stopwords.words("english"))
filtered_list=[]
for j in lema_list:
    if j not in stop:
        filtered_list.append(j)


print(filtered_list)                    #print stop_word,filtered text from here