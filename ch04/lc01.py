def count_nested_levels(nested_documents, target_document_id, level=1):
    if not nested_documents:
        return -1
    
    for key in nested_documents:
        
        if key == target_document_id:
            print(f"\nTarget found in branch: {nested_documents}\nLevel: {level}\n")
            print(f"Returned {level} from key {key}")
            return level
        
        elif nested_documents[key] != {}:
            print(f"Going deeper into key {key} with value {nested_documents[key]}")
            nested_level = count_nested_levels(
                            nested_documents[key],
                            target_document_id, level + 1)
            print(f"Returned {nested_level} from key {key}")
            
            if nested_level != -1:
                return nested_level
    
    return -1

## Testing:

test_tree = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}
target_id = 9

print("\n")
print(f"Running count_nested_levels with:",
      f"\nnested_documents: {test_tree}",
      f"\ntarget_id: {target_id}\n")
print(f"\nResult: {count_nested_levels(test_tree, target_id)}")
print("\n")
