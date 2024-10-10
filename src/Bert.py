from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# BERT model, tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


def get_bert_embedding (text) :
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)

    with torch.no_grad () :
        outputs = model(**inputs)
        
    return outputs.last_hidden_state[:, 0, :].numpy()


def Bert_similarity (title, content) :
    title_embedding = get_bert_embedding(title)
    content_embedding = get_bert_embedding(content)
    
    similarity = cosine_similarity(title_embedding, content_embedding)
    
    return similarity[0][0]


if (__name__ == "__main__") :

    title = "제목"
    content = "제목과 관련된 내용"
    
    similarity = Bert_similarity(title, content)
    print(f"{similarity*100 : .1f}")
