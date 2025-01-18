def deduplicate_lists_bad(list1, list2, rev=False):
    mdict = dict()
    output = list1 + list2
    for item in output:
        mdict.update({item : ""})
    output = list(mdict)
    output = sorted(output, reverse=rev)
    return output

def deduplicate_lists(list1, list2, rev=False):
    return sorted(set(list1 + list2), reverse=rev)