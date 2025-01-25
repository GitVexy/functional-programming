def new_collection(initial_docs):
    docs = initial_docs.copy()
    
    def add_string(s):
        docs.append(s)
        return docs

    return add_string




print(new_collection(["test", "test2"]))
