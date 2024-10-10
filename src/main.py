import json
import os

from Cosine import Cosine_similarity
from Bert import Bert_similarity
from Sbert import Sbert_similarity


if (__name__ == "__main__") :

    input_file = "../data/Crawling_DB/test_data.json"
    output_file = "../data/Ready_DB/test_data.json"

    
    with open(input_file, "r") as file : 
        data = json.load(file)


    similarity = Cosine_similarity(data["title"], data["content"])
    data["Cosine_Similarity"] = float(f"{(similarity * 100) : .1f}")

    similarity = Bert_similarity(data["title"], data["content"])
    data["Bert_Similarity"] = float(f"{(similarity * 100) : .1f}")

    similarity = Sbert_similarity(data["title"], data["content"])
    data["Sbert_Similarity"] = float(f"{(similarity * 100) : .1f}")

    
    with open(output_file, "w") as file :
        json.dump(data, file, indent=4)

    # os.remove(input_file)
    
    print("Done")
