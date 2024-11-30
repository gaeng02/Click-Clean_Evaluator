from konlpy.tag import Okt

def Split_sentence (sentence) :
    
    filtered = sentence.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')

    token = Okt.pos(sentence, stem = True)

    filtered_token = [word for word, tag in token if tag not in ["Josa", "Punctuation", "Suffix"]]
    return_token = [word for word in filtered_token if word not in ["있다"]] 

    return return_token


def Print (word, num, size) :
    for i in range (size) :
        print(word[i], num[i])
    

if (__name__ == "__main__") :

    Okt = Okt()

    title = ""
    
    sentences = [    ]

    word_counts = {}

    for sentence in sentences :

        token = Split_sentence(sentence)

        for word in token :
            
            if word in word_counts : word_counts[word] += 1
            else : word_counts[word] = 1

    
    max_level = max(word_counts.values())

    pixels = 0
    pixel_level = [0] * (max_level + 1)
    
    for item, value in word_counts.items() :
        
        pixels += value
        pixel_level[value] += value


    cumulative_sum = 0
    cdf = [0] * (max_level + 1)
    
    for i in range (max_level) :
        cumulative_sum += pixel_level[i+1]
        cdf[i+1] = round(cumulative_sum * max_level / pixels, 6)

    norm_cdf = [0] * (max_level + 1)
    for i in range (max_level) :
        norm_cdf[i+1] = round(cdf[i+1] / max_level, 5)



    _title = Split_sentence (title)

    score = 0
    count = 0

    for word in _title :
        if word in word_counts : 
            value = word_counts[word]
            score += norm_cdf[value] 
            count += 1

    if count > 0 :
        score /= count

    print(score)
