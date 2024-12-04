from gensim.summarization.summarizer import summarize

def summarize_text (text) :
    
    # length = len(text)
    # 50~100 => 80
    # return summarize(text, ratio = min(0.2, 80 / length))
    
    try : return summarize(text, ratio = 0.2)
    except : return ""
