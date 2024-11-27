import json
import os
from bs4 import BeautifulSoup

# from Evaluator import evaluation
# from Summary import summary


if (__name__ == "__main__") :

    input_file = "../data/Crawling_DB/test.json"
    output_file = "../data/Ready_DB/test.json"

    
    with open(input_file, "r", encoding='utf-8') as file : 
        data = json.load(file)

    title = data["title"]
    
    raw_contents = data["raw_contents"]
    soup = BeautifulSoup(raw_contents, "html.parser")
    plain_text = soup.get_text()

    # summary_text = summary(plain_text)
    summary_text = "test_summary"
    
    # similarity = evaluation(title, plain_text) * 100
    similarity = 81.5

    data["summary"] = summary_text
    data["similarity"] = similarity
    
    with open(output_file, "w", encoding = "utf-8") as file :
        json.dump(data, file, indent = 4, ensure_ascii = False)
              
    print("Done")
