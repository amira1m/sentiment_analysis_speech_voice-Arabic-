Arabic Speech Sentiment Analysis — Android App
An Android application that records Arabic speech, transcribes it in real time, and classifies the sentiment of the spoken text as positive or negative.
What it does
The app listens to the user's voice, converts the Arabic speech to text, then runs an NLP-based sentiment analysis model on the recognized text to determine whether the speech carries a positive or negative sentiment.
How it works

Speech Recognition — Captures and transcribes Arabic voice input in real time using Android's speech recognition API
NLP Processing — Passes the transcribed Arabic text through a sentiment analysis pipeline that handles Arabic morphological complexity
Classification — Outputs whether the speech is positive or negative sentiment

Project Structure

MyApplication15/ — Android app (Kotlin)
text/ — Python NLP model and sentiment analysis logic

Tech Stack

Kotlin (Android)
Python
TensorFlow
NLTK / SpaCy
Android Studio
