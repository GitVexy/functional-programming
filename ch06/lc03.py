def css_styles(initial_styles: dict):
    styles = initial_styles.copy()
    
    def add_style(selector: str, property: str, value: str) -> dict:
        if selector not in styles:
            styles[selector] = {property: value}
        else:
            styles[selector][property] = value

        return styles
    
    return add_style
