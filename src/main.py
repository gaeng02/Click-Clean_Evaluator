import json
import os
import re
from bs4 import BeautifulSoup

from evaluate.Comparison import evaluation
from summary.Summarization import summarize_text
from extract_sentence import extract_as_list, extract_as_str 

    
if (__name__ == "__main__") :

    input_path = "../data/Crawling_DB"
    output_path = "../data/Ready_DB"
    
    for filename in os.listdir(input_path) :

        try : 
        
            input_file = os.path.join(input_path, filename)
            
            with open(input_file, "r", encoding='utf-8') as file : 
                data = json.load(file)

            title = data["title"]
            
            body = data["body"]
            soup = BeautifulSoup(body, "html.parser")

            text_content = soup.get_text()

            # need to call "extract_sentence.py" to change contents to sentence list

            summary_text = summarize_text(extract_as_str(text_content))

            similarity = round(evaluation(title, extract_as_list(text_content)) * 100, 3)

            '''
            if summary_text == "" :
                print("Null Summary", filename)
                print(extract_as_str(text_content))
            '''

            data["summary"] = summary_text
            data["probability"] = similarity

            output_file = os.path.join(output_path, filename)
            
            with open(output_file, "w", encoding = "utf-8") as file :
                json.dump(data, file, indent = 4, ensure_ascii = False)

        except :
            # print(filename)
            continue

    # print("All Done")
