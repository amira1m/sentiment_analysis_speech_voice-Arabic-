import json
import tensorflow as tf
import pandas as pd
import numpy as np
import codecs
# from flask import Flask
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

vocab_size = 7753
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 6700

df = pd.read_csv('Train.csv', encoding='utf-8')
df = df.drop(['ID'], axis=1)

sentences = []
labels = []
sentences = df['Feed'].astype(str)
labels = df['Sentiment'].astype(str)
values = np.array(labels)

# Encoding labels
# print(values)
# integer encode
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(values)
# print(labels)

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
testing_labels = labels[training_size:]

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index

# training_sequences = tokenizer.texts_to_sequences(training_sentences)
# training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
#
# testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
# testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

# print(training_padded)
# print(training_sequences)

# training_padded = np.array(training_padded)
# training_labels = np.array(training_labels)
# testing_padded = np.array(testing_padded)
# testing_labels = np.array(testing_labels)


# model1 = tf.keras.Sequential([
#     tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
#     tf.keras.layers.GlobalAveragePooling1D(),
#     tf.keras.layers.Dense(24, activation='relu'),
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])
# model1.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
# model1.summary()

# num_epochs = 30
# history = model1.fit(training_padded, training_labels, epochs=num_epochs, validation_data=(testing_padded, testing_labels), verbose=2)

# loaded_model = tf.keras.models.load_model("my_model")
#
# sentence = ["تمام "]
# sequences = tokenizer.texts_to_sequences(sentence)
# padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
# print(loaded_model.predict(padded))

# model1.save("my_model")

