from gensim.summarization.summarizer import summarize

def summarize_text (text, _ratio = 0.1) :
    return summarize(text, ratio = _ratio)

if __name__ == "__main__":

    text = ""
    
    print(summarize_text (text, 0.2))
