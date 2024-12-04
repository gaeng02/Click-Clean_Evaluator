import json
import time
import boto3
import pymysql
from bs4 import BeautifulSoup

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

        data["summary"] = summarize_text(extract_as_str(text_content))

        data["probability"] = round(evaluation(title, extract_as_list(text_content)) * 100, 3)

        post_to_rds(data)

    except Exception as e :
        print(e)


def lambda_handler (event, context) :
    
    for record in event['Records'] :
        process_message(record)
        
