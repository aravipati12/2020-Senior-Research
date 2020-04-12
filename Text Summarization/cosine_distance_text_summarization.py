from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

def read_article(file_name): # return dictionary of sentences split word by word
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        helper = ''.join([i for i in sentence if (i.isalpha() or i == " ")]) # no punctuation
        helper = helper.replace("  ", " ") # dashes and stuff
        sentences.append(helper.split(" "))

    return sentences

def sentence_similarity(one, two, stopwords): # similarity between words using cosine distance
    one = [w.lower() for w in one]
    two = [w.lower() for w in two]

    combined = list(set(one + two))

    v1 = [0] * len(combined)
    v2 = [0] * len(combined)

    for word in one:
        if word not in stopwords:
            v1[combined.index(word)] += 1

    for word in two:
        if word not in stopwords:
            v2[combined.index(word)] += 1

    return 1 - cosine_distance(v1, v2)

def build_graph(sentences, stop_words): # builds graph of similarity between sentences
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 != idx2: # not same sentence
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name, summary_length): # builds summary
    stop_words = stopwords.words('english') # first person and stuff
    summarize_text = []

    sentences =  read_article(file_name)
    scores = nx.pagerank(nx.from_numpy_array(build_graph(sentences, stop_words))) # numpy yeet

    sentences_ranked = []
    for i, s in enumerate(sentences):
        sentences_ranked.append((scores[i], s))
    sentences_ranked = sorted(sentences_ranked)
    for i in range(summary_length): # summary length
      summarize_text.append(" ".join(sentences_ranked[len(sentences_ranked) - i - 1][1]))

    summary = ". ".join(summarize_text) + "."
    print(summary)
    file = open("summary.txt", "w+")
    file.write(summary)
    file.close()

generate_summary("transcript.txt", 4)
