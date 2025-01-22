def word_count_memo(document: str, memos: dict) -> tuple[int, dict]:
    local_memos = memos.copy()

    if document in local_memos.keys():
        return local_memos[document], local_memos
    else:
        local_memos[document] = word_count(document)
    
    return local_memos[document], local_memos



# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
