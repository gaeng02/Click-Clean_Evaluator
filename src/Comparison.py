import json
import os
from konlpy.tag import Okt

Okt = Okt()

def Split_sentence (sentence) :
    
    filtered = sentence.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')

    token = Okt.pos(sentence, stem = True)

    filtered_token = [word for word, tag in token if tag not in ["Josa", "Punctuation", "Suffix"]]
    return_token = [word for word in filtered_token if word not in ["있다"]] # removed_useless tag

    return return_token


def evaluation (title, sentences) :
    '''
    Extract features
    - TF-IDF and cosine similarity
    - Adverb, Adjective ratio
    '''

    
    '''
    evaluation code
    - "../evaluation_model/unsupervised.py"
    - "../evaluation_model/semi_supervised.py"
    - "../evaluation_model/supervised.py"
    '''

    return score

    
