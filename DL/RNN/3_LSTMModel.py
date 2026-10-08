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


#step 6 function to decode the revies (number to  word)
# 
def DecodeReview(encoded_review):
    words=[] 
    for number in encoded_review:
        if number >=3:   #ignore first 3
            word=reverse_word_index.get(number,"?") 
            words.append(word)
    return " ".join(words)# join tge list of words


#step 7 Display sample reviews 
print("-"*40)
print("----------------------Sample Reviews--------------------------- ")
print("-"*40)


for i in range (3,7):
    review = DecodeReview(X_train[i])

    print("Review number :",i+1)
    print("Review:")
    print(review)

    if Y_train[i]==1:
        print("Sentimental: POSITIVE")
    else:
        print("Sentimental : NEGATIVE")


 

#step 8 padding 
# 
X_train_padded=pad_sequences(
    X_train,
    maxlen = MAX_LENTH
)  

X_test_padded=pad_sequences(
    X_test,
    maxlen=MAX_LENTH
)

print("treining data shape :",X_train_padded.shape)
print("testing data shape :",X_test_padded.shape)

#step 9 creTE LSTM model

model=Sequential()
model.add(
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=32  #each word is represended in 32 values

    )
)

model.add(
    LSTM(
        units=64 #size of lstm hidden state
    )
)
model.add(
    Dense(
        units=1,
        activation="sigmoid" #use to produce probabality
    )
)


#project Architecture

#Review -> Embedding -> LSTM -> Dence -> sigmoid -> positive/Negarive

#step 10 compile the model

model.compile(
    optimizer="adam" ,# algoritham to update weights
    loss="Binary_crossentropy",#loss function
    metrics=["accuracy"]

)
print("model compile ")

#step 11 train the model 

print("model training")

model.fit(
    X_train_padded,#input training review
    Y_train,        #actual sentiment label
    epochs=3,        #complete dataset gets processes 3 items
    batch_size=64,   # process g4 review in one batch
    validation_split=0.2 #use 20% training for validation


)

print("model training gets complited")

#step 12 : Evaluate the model

accuracy= model.evaluate(
    X_test_padded,     #testing reviews
    Y_test,             #Actual testing labels 
    verbose =0          #dont display the process bar 
)

print("testing Accuracy :",accuracy)

#step 13 predict the review
TEST_REVIEW_NUMBER = 0

original_review=X_test[TEST_REVIEW_NUMBER]
decoded_review=DecodeReview(original_review)

print("Review given to the model:")
print(decoded_review)

#step 14 get the actual sentiment 
actual_value=Y_test[TEST_REVIEW_NUMBER]
if actual_value==1:
    actual_sentiment="POSITIVE"
else:
    actual_sentiment="NEGATIVE"

print("Actual sentiment ",actual_sentiment)

#step 15 predict the sentiment 

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER : TEST_REVIEW_NUMBER+1]

prediction=model.predict(
    review_for_prediction,
    verbose=0
)
probabality = prediction[0][0]

if probabality >= 0.5:
    predicted_sentiment="positive"
else:
    predicted_sentiment="NEGATIVE"

print("final result")
print("prediction probabality:",probabality)
print("actual sentiment :",actual_sentiment)
print("predicted sentiment:",predicted_sentiment)










