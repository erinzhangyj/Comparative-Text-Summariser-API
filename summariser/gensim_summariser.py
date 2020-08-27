from gensim.summarization.summarizer import summarize

def get_summary(text):
    summary = summarize(text, ratio=0.005)
    return summary