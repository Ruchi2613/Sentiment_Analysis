'''
1.This line imports the Streamlit library and gives it an alias st for convenience.
 Streamlit is a Python library that allows you to create interactive web apps with minimal code.
 The st is the alias used to call various Streamlit functions throughout the code (e.g., st.title, st.text_area).

2. I'm importing the pipeline function from the Hugging Face Transformers library.
This function helps you load pre-trained machine learning models for various tasks like sentiment analysis,
translation, and more. In this case, you'll use it for sentiment analysis.
'''
import streamlit as st
from transformers import pipeline

'''This line loads a pre-trained sentiment analysis model using the pipeline function from Hugging Face's Transformers library. 
It tells the program to load a model that can perform sentiment analysis on text.'''

'''By specifying "sentiment-analysis", I'm telling the model to analyze the sentiment of text, i.e.,
 whether the text is positive, negative, or neutral.'''
sentiment_model = pipeline("sentiment-analysis")


'''This line creates the title of the web app using Streamlit.
 It displays "Sentiment Analysis App" as the main heading at the top of the page.'''
st.title("Sentiment Analysis App")

# Text input from the user
user_input = st.text_area("Enter text to analyze sentiment:")

'''This creates a clickable button in the app labeled "Analyze". When the user clicks this button, it triggers an action.'''
if st.button("Analyze"):
    result = sentiment_model(user_input)[0]
    '''
     pipeline("sentiment-analysis") method, the model typically returns a list of dictionaries, even though it usually contains only one dictionary.

    '''
    '''sentiment_model(user_input): This calls the pre-trained model that was loaded earlier (sentiment_model) and passes the user's input (user_input) to it. The model will analyze the sentiment of the entered text.
The model returns a list of results, but since I'm interested in the first result (there’s usually only one), you access it using [0]. This gives you the sentiment analysis result for the input.
'''
    sentiment = result['label']
    score = result['score']
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Confidence:** {score:.2f}")

'''st.write(f"**Sentiment:** {sentiment}"): This line displays the sentiment result (whether it's positive, negative, or neutral) on the web page.
f"**Sentiment:** {sentiment}": This is an f-string that inserts the sentiment value into the string so it can be displayed dynamically.

st.write(f"**Confidence:** {score:.2f}"): This line displays the confidence score with a precision of two decimal places.
{score:.2f}: This formats the score to display only two decimal places.'''