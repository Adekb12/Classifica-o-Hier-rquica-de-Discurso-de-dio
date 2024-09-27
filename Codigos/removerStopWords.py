import nltk
from nltk.corpus import stopwords

from gensim.parsing.preprocessing import remove_stopword_tokens
from gensim.parsing.preprocessing import STOPWORDS

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))
portuguese_stop_words = STOPWORDS.union(set(stop_words))

def remove_stop_words(tokens):
    return remove_stopword_tokens(tokens, stopwords=portuguese_stop_words)

import pandas as pd
tweets = pd.read_csv('C:\\Users\\marde\\OneDrive\\Documentos\\CC\\Mineracao_de_Dados\\dataset_Paula_Fortuna\\tweets_tokenizados.csv')

noStopWords = pd.DataFrame({
    'tokens': tweets['tokens'].apply(eval).apply(remove_stop_words), 
    'class': tweets['class']})

noStopWords.to_csv('tweets_noStopWords.csv', index=True)
#print(noStopWords)

