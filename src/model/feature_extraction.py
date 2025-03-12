'''
- TF-IDF -> Cosine Similarity
- Adverb, Interjection ratio
'''

import numpy as np
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_cosine (title : str, content : str) :
    
    vectorizer = TfidfVectorizer()
    vectorizer.fit([title, content])
    
    title_vec = vectorizer.transform([title])
    body_vec = vectorizer.transform([body])
    
    similarity = cosine_similarity(title_vec, body_vec)[0, 0]
    return similarity


okt = Okt()

def get_ratio (title) :
    
    tokens = okt.pos(title)
    total = len(tokens) if tokens else 1
    
    cnt = 0 # for count adverb, interjection
    
    for _, pos in tokens :
        if pos in ["Adverb", "Exclamation"] :
            cnt += 1

    
    ratio = cnt / total
    
    return ratio
