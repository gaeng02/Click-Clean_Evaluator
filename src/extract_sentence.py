import re

def extract_as_list (text) : 

    result_list = []
    
    cleaned_list = re.sub(r"[\n\t\r]+", ".", text.strip())

    reduced_list = re.split(r"[.!?]", cleaned_list)

    for sentence in reduced_list :
        s = sentence.strip()
        if s : result_list.append(s)

    return result_list

def extract_as_str (text) : 

    result_text = re.sub(r"[\n\t\r]+", " ", text.strip())

    return result_text


if (__name__ == "__main__") :
    
    text =""
    
    _list = extract_as_list (text)
    _str = extract_as_str (text)
