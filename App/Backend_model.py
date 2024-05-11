import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import pandas as pd 
import numpy as np
import json
import random
import tkinter as tk
import spacy
import nltk

nlp = spacy.load('en_core_web_lg')
stemmer = nltk.PorterStemmer()

with open('D:\\HWAN\\Data\\Main_chatbot_dataset.json','r') as f1:
    data1 = json.load(f1)
    
with open('D:\\HWAN\\Data\\Mental_health_conversation.json','r') as f2:
    data2 = json.load(f2)

with open('D:\\HWAN\\Data\\First_Aid_recommendation.json','r') as f3:
    data3 = json.load(f3)

data4 = pd.read_csv(r'D:\HWAN\Data\Symptom_checker_dataset\disease_description.csv')
data5 = pd.read_csv(r'D:\HWAN\Data\Symptom_checker_dataset\disease_precaution.csv')

def stem(sentence):
    tokens = nltk.word_tokenize(sentence)
    stemmed_tokens = []
    
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    
    return ' '.join(stemmed_tokens)

def MainChatbot(chat_display,user_input):
    user_message_ = user_input.get()
    chat_display.insert(tk.END, "You: " + user_message_ + "\n")
    user_input.delete(0,tk.END)
    user_message = stem(user_message_)
    user_message = nlp(user_message).vector
    user_message = np.array(user_message)
    user_message = np.reshape(user_message, (1, 300, 1))
    user_message = tf.convert_to_tensor(user_message)
    model = tf.keras.models.load_model(r'D:\HWAN\Models\Main_chatbot_Model\M_CBOT_M.keras')
    predictions = model.predict(user_message)
    predicted_class_index = np.argmax(predictions)
    predicted_class_probability = predictions[0][predicted_class_index]
    if predicted_class_probability > 0.5:
        if predicted_class_index == 5:
            chat_display.insert(tk.END, 'H.W.A.N: ' + random.choice(data1['intents'][predicted_class_index]['responses']) + '\n')
            with open('D:\\HWAN\\Data\\Suggestions.csv','a') as f_1:
                f_1.write(user_message_)
        elif predicted_class_index == 6:
            chat_display.insert(tk.END, 'H.W.A.N: ' + random.choice(data1['intents'][predicted_class_index]['responses']) + '\n')
            with open('D:\\HWAN\\Data\\Bug_report.csv','a') as f_2:
                f_2.write(user_message_)
        elif predicted_class_index == 8:
            chat_display.insert(tk.END, 'H.W.A.N: ' + random.choice(data1['intents'][predicted_class_index]['responses']) + '\n')
            with open('D:\\HWAN\\Data\\Feedback.csv','r') as f_3:
                f_3.write(user_message_)
        else:
            chat_display.insert(tk.END, 'H.W.A.N: Can you please rephrase what are you trying to say?'+'\n')

def SyncZen_(chat_display,user_input):
    user_message = user_input.get()
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    user_input.delete(0,tk.END)
    user_message = stem(user_message)
    user_message = nlp(user_message).vector
    user_message = np.array(user_message)
    user_message = np.reshape(user_message, (-1,1,300))
    user_message = tf.convert_to_tensor(user_message)
    model = tf.keras.models.load_model(r'D:\HWAN\Models\Stress_Mental_Health_Conversation_Chatbot\SyncZenModel.keras')
    predictions = model.predict(user_message)
    predicted_class_index = np.argmax(predictions)
    predicted_class_probability = predictions[0][predicted_class_index]
    if predicted_class_probability > 0.5:
        chat_display.insert(tk.END, 'SyncZen: ' + random.choice(data2['intents'][predicted_class_index]['responses']) + '\n')
    else:
        chat_display.insert(tk.END, 'SyncZen: Can you please rephrase what are you trying to say?'+'\n')

def clean(sentence):
    tokens = []
    doc = nlp(sentence)
    for token in doc:
        if token.is_alpha:
            tokens.append(str(token))
    return ' '.join(tokens)

def AidSync(chat_display,user_input):
    user_message = user_input.get()
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    user_input.delete(0,tk.END)
    user_message = clean(user_message)
    user_message = nlp(user_message).vector
    user_message = np.array(user_message)
    user_message = np.reshape(user_message, (-1,1,300))
    user_message = tf.convert_to_tensor(user_message)
    model = tf.keras.models.load_model(r'D:\HWAN\Models\First_Aid_Recommendations\AidSyncModel.keras')
    predictions = model.predict(user_message)
    predicted_class_index = np.argmax(predictions)
    predicted_class_probability = predictions[0][predicted_class_index]
    if predicted_class_probability > 0.5:
        chat_display.insert(tk.END, 'AidSync: ' + random.choice(data3['intents'][predicted_class_index]['responses']) + '\n')
    else:
        chat_display.insert(tk.END, 'AidSync: Can you please rephrase what are you trying to say?'+'\n')

def Symptom_checker(chat_display,user_input):
    user_message = user_input.get()
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    user_input.delete(0,tk.END)
    sentence = clean(user_message)
    sentence = nlp(sentence).vector
    sentence_ = np.reshape(sentence, (1, 300, 1))
    sentence = np.reshape(sentence,(-1, 1, 300))
    sentence = tf.convert_to_tensor(sentence)
    model = tf.keras.models.load_model(r'D:\HWAN\Models\Symptom_checker_Models\SCM(Final).keras')
    predictions = model.predict(sentence)
    predicted_class_index = np.argmax(predictions)
    predicted_class_probability = predictions[0][predicted_class_index]
    model_ = tf.keras.models.load_model(r'D:\HWAN\Models\Main_chatbot_Model\M_CBOT_M.keras')
    predictions_ = model_.predict(sentence_)
    predicted_class_index_ = np.argmax(predictions_)
    predicted_class_probability_ = predictions_[0][predicted_class_index_]
    if predicted_class_probability > predicted_class_probability_:
        if predicted_class_probability > 0.5:
            search_value = predicted_class_index
            result = data5[data5['numeric_label'] == search_value]
            result_2 = data4[data4['Disease'] == result['Disease'].iloc[0]]
            printed_result = f'It seems that you are suffering from {result_2["Disease"].iloc[0]}:\n {result_2["Symptom_Description"].iloc[0]} \n Some Precautions that you can take are: \n 1){result["Symptom_precaution_0"].iloc[0]} \n 2){result["Symptom_precaution_1"].iloc[0]} \n 3){result["Symptom_precaution_2"].iloc[0]}'
            chat_display.insert(tk.END, 'Pulse: ' + printed_result + '\n')
        else:
            chat_display.insert(tk.END, 'Pulse: Can you please rephrase what are you trying to say?'+'\n')
    else:
        if predicted_class_index_ == 0:
            chat_display.insert(tk.END, 'Pulse: ' + random.choice(data1['intents'][0]['responses']) +'\n')
        elif predicted_class_index_ == 11:
            chat_display.insert(tk.END, '''Pulse: I'm pulse part of project H.W.A.N and I'm here to check your symptoms to provide you assistance in identifying the disease and help cure it''' + '\n')
        else:
            chat_display.insert(tk.END, 'Pulse: Can you please rephrase what are you trying to say?'+'\n')