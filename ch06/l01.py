def word_count_aggregator():
    count = 0

    def word_counter(doc: str):
        nonlocal count
        count += len(doc.split())
        return count
    
    return word_counter
