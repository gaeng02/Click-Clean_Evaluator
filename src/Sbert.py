from sentence_transformers import SentenceTransformer, util

'''
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
'''

# SBERT model 
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def Sbert_similarity (title, content) :
    # 제목과 내용 임베딩 생성
    title_embedding = model.encode(title, convert_to_tensor = True)
    content_embedding = model.encode(content, convert_to_tensor = True)
    
    # 코사인 유사도 계산
    similarity = util.pytorch_cos_sim(title_embedding, content_embedding)
    
    return similarity.item()


if (__name__ == "__main__") :

    title = "제목"
    content = "제목과 관련된 내용"
    
    similarity = Sbert_similarity(title, content)
    print(f"{similarity*100 : .1f}")
