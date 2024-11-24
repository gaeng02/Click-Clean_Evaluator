from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def Cosine_similarity (title, content) :
    texts = [title, content]
    
    # TF-IDF vectorize 
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # calculate
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return similarity[0][0]  


if (__name__ == "__main__") :

    title = "제목"
    content = "제목과 관련된 내용"
    
    similarity = Cosine_similarity(title, content)
    print(f"{similarity*100 : .1f}")
