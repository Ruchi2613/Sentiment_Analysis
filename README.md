# Sentiment Analysis with Hugging Face and Streamlit

This project demonstrates how to perform sentiment analysis using the Hugging Face Transformers library and deploy the model through a simple Streamlit web application. The model will analyze the sentiment of user-provided text, classifying it as positive, negative, or neutral.

## Steps to Set Up and Run the Project

### 1. **Install Python and Create a Virtual Environment**

First, ensure that you have Python 3.6 or later installed on your machine. It’s always a good practice to use a virtual environment to manage project dependencies.

- To create a virtual environment, run:
  ```bash
  python3 -m venv .venv


#Activate the virtual environment:
#source .venv/bin/activate

**Install Required Libraries**
We need the following libraries for the project:

Transformers: A library by Hugging Face to easily access pre-trained machine learning models for Natural Language Processing (NLP).
Streamlit: A framework to quickly create interactive web applications.
TensorFlow or PyTorch: Deep learning frameworks required by Transformers to run models.
Run the following commands to install the necessary libraries:

Install Transformers: pip install transformers
-> The transformers library is used to access pre-trained models for NLP tasks like sentiment analysis. We need this to easily load the model and make predictions.

**Install Streamlit**
-> pip install streamlit
Streamlit is a tool that allows us to turn Python scripts into interactive web apps with just a few lines of code. It’s used here to provide a UI where users can input text and get the sentiment prediction.

**Install Deep Learning Framework (PyTorch or TensorFlow)**
 install TensorFlow:
pip install tensorflow
-> The Hugging Face models require either PyTorch or TensorFlow to run. These frameworks are needed because they provide the backend for processing the machine learning models.

**Install Additional Dependencies (if necessary)**
In case of version issues with Keras (a dependency of TensorFlow), install the backward-compatible version:
pip install tf-keras
-> The Transformers library expects a version of Keras that is compatible with TensorFlow. This command installs the correct version.

**4. Run the Streamlit Application**
After installing all dependencies, run the Streamlit application with:
streamlit run app.py
-> This command starts the web application, which allows users to interact with the model through a simple UI to input text and get sentiment analysis results.

**Output:**

Input: "I love using Hugging Face models!"
Output: {'label': 'POSITIVE', 'score': 0.9998}