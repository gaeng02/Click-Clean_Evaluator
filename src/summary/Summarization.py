from gensim.summarization.summarizer import summarize

def summarize_text (text) :
    
    length = len(text)
    # 50~100 => 80
    return summarize(text, ratio = min(1, 80 / length))


if __name__ == "__main__":

    text = ""
    
    # print(summarize_text (text, 0.2))
