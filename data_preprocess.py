import pandas as pd
import os
from langdetect import detect, DetectorFactory
folder_path='data'
file_path=os.path.join(folder_path,'positive10k.txt')

output_folder_path = 'output'

df_doc=pd.DataFrame()
df_doc['Text'] = []
df_doc['Sentiment'] = []

df_sent=pd.DataFrame()
df_sent['Text'] = []
df_sent['Sentiment'] = []

df_edu=pd.DataFrame()
df_edu['Text'] = []
df_edu['Sentiment'] = []

def isValidate(text):

        valid_len = len(text) > 1
        not_empty = len(text.rstrip().split()) > 0

        # check line content -> sentence
        sentences = [sent.strip() for sent in text.strip().split(".")]
        valid_sentences = [sent for sent in sentences if sent != ""]
        if len(valid_sentences) == 1: return False

        if valid_len and not_empty:
            try:
                is_en = detect(text) == 'en'
                return is_en
            except Exception as e:
                return "Error: " + str(e)
        else: 
            return False

with open(file_path,'r') as file:
    # file_content=file.read()
    for line in file:
        # check 
        if (isValidate(line)):
            df_doc.loc[len(df_doc.index)] = [line, 1]
        # sentences=line.strip().split('.')
        # for sentence in sentences:
        #     if(isValidate(sentence)):
        #         df.loc[len(df.index)] = [sentence, 1]
                

    print("Produce document-level data with shape", df_doc.shape)
    df_doc.to_csv(os.path.join(output_folder_path,'document.csv'), index=False)

    print("Produce sentence-level data with shape", df_sent.shape)
    df_sent.to_csv(os.path.join(output_folder_path,'sentence.csv'), index=False)

    print("Produce EDU-level data with shape", df_edu.shape)
    df_edu.to_csv(os.path.join(output_folder_path, 'edu.csv'), index=False)

