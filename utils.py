def clean_text(text):
    """
    Basic text cleaning function.
    Keeps the logic simple for clarity and explainability.
    """
    if text is None:
        return ""
    
    return text.lower().strip()
