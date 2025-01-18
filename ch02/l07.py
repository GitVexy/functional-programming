from functools import reduce


def join(doc_so_far, sentence):
    return ". ".join([doc_so_far, sentence])


def join_first_sentences(sentences, n):
    if not sentences or n == 0: return ""
    return reduce(join, sentences[:n]) + "."
