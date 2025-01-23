def list_files(parent_directory, current_filepath="/"):
    filepaths = []

    for key in parent_directory.keys():
        if isinstance(parent_directory[key], dict):
            new_filepath = current_filepath + str(key) + "/"
            filepaths.extend(list_files(parent_directory[key], new_filepath))

        elif parent_directory[key] is None:
            filepaths.append(current_filepath + str(key))
    
    return filepaths

print(list_files({
    'Documents': {
        'Proposal.docx': None,
        'Report': {
            'AnnualReport.pdf': None, 'Financials.xlsx': None}},
    'Downloads': {
        'picture1.jpg': None, 'picture2.jpg': None}}))