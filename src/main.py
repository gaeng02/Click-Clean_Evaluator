import json
import time
import boto3
import pymysql
from bs4 import BeautifulSoup
import os

from Comparison import evaluation
from Summarization import summarize_text
from extract_sentence import extract_as_list, extract_as_str


def post_to_rds (data) : 

    try :
        # have to set !!!
        conn = pymysql.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )

        with conn.cursor() as cursor :
            
            sql = """
                INSERT INTO news_data (title, body, summary, author, url, category, created_at, probability)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(sql, (
                data["title"],       
                data["body"],        
                data["summary"],  
                data["media"],   
                data["author"],    
                data["url"],      
                data["category"],  
                data["created_at"],  
                data["probability"]
            ))
            
        connection.commit()
        
    except Exception as e :
        print(e)
        
    finally :
        if connection :
            connection.close()


def process_message (message) :

    try :
        data = json.loads(message)

        title = data["title"]
        
        body = data["body"]
        soup = BeautifulSoup(body, "html.parser")
        text_content = soup.get_text()

        body_string = extract_as_str(text_content)
        body_list = extract_as_list(text_content)

        data["summary"] = summarize_text(body_string)
        if (data["summary"] == False) :
            data["summary"] = body_list[0]

        data["probability"] = round(evaluation(title, body_list) * 100, 3)

        # post_to_rds(data)
        save_as_json(data)

    except Exception as e :
        print(f"{e} :: {message}")


def save_as_json () :

    input_path = "../data/Crawling_DB"

    for filename in os.listdir(input_path) :

        try : 
            file = os.path.join(input_path, filename)

            with open(file, "r", encoding='utf-8') as datafile : 
                data = json.load(datafile)
                
            title = data["title"]
            
            body = data["body"]
            soup = BeautifulSoup(body, "html.parser")
            text_content = soup.get_text()

            body_string = extract_as_str(text_content)
            body_list = extract_as_list(text_content)

            data["summary"] = summarize_text(body_string)
            if (data["summary"] == "") :
                data["summary"] = body_list[0]

            data["probability"] = round(evaluation(title, body_list) * 100, 3)
            
                
            output_path = "../data/Ready_DB/"
            output_file = os.path.join(output_path, filename)

            with open(output_file, "w", encoding = "utf-8") as datafile :
                json.dump(data, datafile, indent = 4, ensure_ascii = False)
                
        except Exception as e :
            print(f"{e} :: {filename}")
    
    

def lambda_handler (event, context) :
    
    for record in event['Records'] :
        process_message(record)

if (__name__ == "__main__") : 
    save_as_json()
    print("Done")
