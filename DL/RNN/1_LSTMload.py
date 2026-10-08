# import required Libraries
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding ,LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences


#step 2 configuraton of values 


VOCAB_SIZE=10000   # consider moast frequent 10000 unique words
MAX_LENTH = 200    # consider maximum 200 word in review

#step 3 load tghe IMDB dataset 
print("-"*40)
print("movie Sentiment analysis using lstm")
print("-"*40)


print("load the data ")
(X_train,Y_train),(X_test,Y_test)=imdb.load_data(num_words=VOCAB_SIZE)
print("IMDB dataset load sucesfully")

print("number of training reviev",len(X_train))
print("number od testinf revievs",len(X_test))

#X_train         Reviews  used for training
#Y_train         Actual sentiments of training 
#X_test          Reviews  used for testing

#Y_test           ctual sentiments of testing


#0> negative 
#1> positive


#step 4 load the word dectonary





word_index=imdb.get_word_index()

#Dictonary contain mapping of word and is corresponding number 
#drisham is good movie   -> (20 56 78 43)
#20 ->  drisham
#56  -> is
#78 -> good
#43 -> movie



#step 5 create revers dictonary

reverse_word_index={}
for word,index in word_index.items():
    reverse_word_index[index+3]=word


