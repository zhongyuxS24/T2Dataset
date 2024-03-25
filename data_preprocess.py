import pandas as pd
import os
import re
from langdetect import detect, DetectorFactory

from segment_data import segment_into_edus


def isValidate(text):

        # text length longer than 1
        valid_len = len(text) > 1
        # check line content -> not empty
        not_empty = len(text.rstrip().split()) > 0

        # check line content -> sentence
        sentences = [sent.strip() for sent in text.strip().split(".")]
        valid_sentences = [sent for sent in sentences if sent != ""]
        if len(valid_sentences) <= 1: return False

        if valid_len and not_empty:
            try:
                is_en = detect(text) == 'en'
                return is_en
            except Exception as e:
                return "Error: " + str(e)
        else: 
            return False

def filter_sentences(sentences):
    filtered_sentences = []
    for sent in sentences:
        splitted = re.split(r'[.,;!?]', sent)
        # Filter out empty strings and whitespace
        splitted = [s.strip() for s in splitted if s.strip() != '']
        if len(splitted) > 1 or (len(splitted) == 1 and len(splitted[0].split()) > 1):
            filtered_sentences.append(sent)
    return filtered_sentences

def filter_edus(edus):
    filtered_edus = []
    for edu in edus:
        splitted = edu.strip().split(" ")
        splitted = [s for s in splitted if s != ""]
        if len(splitted) > 1:
            filtered_edus.append(edu)
    return filtered_edus

def preprocess_data(file_paths, output_folder_path):
    df_doc=pd.DataFrame()
    df_doc['Text'] = []
    df_doc['Sentiment'] = []

    df_sent=pd.DataFrame()
    df_sent['Text'] = []
    df_sent['Sentiment'] = []
    df_sent['Doc_ID'] = []

    df_edu=pd.DataFrame()
    df_edu['Text'] = []
    df_edu['Sentiment'] = []
    df_edu['Doc_ID'] = []

    for i, file_path in enumerate(file_paths):
        with open(file_path,'r') as file:
            # file_content=file.read()
            for line in file:
                # check 
                if (isValidate(line)):
                    df_doc.loc[len(df_doc.index)] = [line, i]
                    sentences, edus = segment_into_edus(line)
                    for sent in filter_sentences(sentences):
                        df_sent.loc[len(df_sent.index)] = [sent, i, len(df_doc.index)]
                    for edu in filter_edus(edus):
                        df_edu.loc[len(df_edu.index)] = [edu, i, len(df_doc.index)]

    df_doc.drop_duplicates(subset=['Text'], inplace=True)
    df_sent.drop_duplicates(subset=['Text'], inplace=True)
    df_edu.drop_duplicates(subset=['Text'], inplace=True)

    print("Produce document-level data with shape", df_doc.shape)
    df_doc.to_csv(os.path.join(output_folder_path,'document.csv'), index=False)

    print("Produce sentence-level data with shape", df_sent.shape)
    df_sent.to_csv(os.path.join(output_folder_path,'sentence.csv'), index=False)

    print("Produce EDU-level data with shape", df_edu.shape)
    df_edu.to_csv(os.path.join(output_folder_path, 'edu.csv'), index=False)

folder_path = "Android-App-Reviews-Dataset"
output_folder_path = 'output'
file_paths = [os.path.join(folder_path, 'negative10k.txt'), os.path.join(folder_path, 'positive10k.txt')]
preprocess_data(file_paths, output_folder_path)