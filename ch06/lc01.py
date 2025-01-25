def new_clipboard(initial_clipboard: dict):
    clipboard = initial_clipboard.copy()
    
    def copy_to_clipboard(key: str, value: str):
        clipboard[key] = value
    
    def paste_from_clipboard(key: str):
        return clipboard[key] if key in clipboard else ""
        
    return copy_to_clipboard, paste_from_clipboard
