


def map_keywords(document, document_map):

    local_map = document_map.copy()

    if document in local_map:
        return local_map[document], local_map
    
    found_keywords = find_keywords(document)
    local_map[document] = found_keywords

    return local_map[document], local_map


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]

    output = []

    for word in keywords:

        if word in document:
            output.append(word)
    
    return output
