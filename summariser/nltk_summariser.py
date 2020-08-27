from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

def word_frequency_table(raw_text):
    #Tokenise words
    tokens = word_tokenize(raw_text.lower())

    #Create word frequency table
    stop_words = stopwords.words("english")
    lemmatiser = WordNetLemmatizer()

    frequency_table = {}
    for word in tokens:
        word = lemmatiser.lemmatize(word)
        if word in stop_words:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1

    return frequency_table

def score_sentences(sentences, frequency_table):
    sentence_value = {}

    for sentence in sentences:
        sentence_word_count = (len(word_tokenize(sentence)))
        for word_val in frequency_table:
            if word_val in sentence.lower():
                if sentence[:10] in sentence_value:
                    sentence_value[sentence[:10]] += frequency_table[word_val]
                else:
                    sentence_value[sentence[:10]] = frequency_table[word_val]

        sentence_value[sentence[:10]] = sentence_value[sentence[:10]]//sentence_word_count

    return sentence_value

def threshold_value(sentence_value):
    val = 0
    for entry in sentence_value:
        val += sentence_value[entry]
    threshold_val = int(val/len(sentence_value))

    return threshold_val

def create_summary(sentences, sentence_value, threshold_value):
    sentence_count = 0
    summary = ""

    for sentence in sentences:
        if sentence_count == 5:
            break
        if sentence[:10] in sentence_value and sentence_value[sentence[:10]]>(threshold_value):
            summary += " " + sentence
            sentence_count += 1

    return summary

def get_summary(text):
    # 1. Generate word frequency table
    frequency_table = word_frequency_table(text)

    #2. Tokenise sentences
    sentences = sent_tokenize(text)

    #3. Score sentences
    sentence_scores = score_sentences(sentences, frequency_table)

    #4. Find the threshold value
    threshold_val = threshold_value(sentence_scores)

    #5. Generate summary
    summary = create_summary(sentences, sentence_scores, 1.5 * threshold_val)

    return summary