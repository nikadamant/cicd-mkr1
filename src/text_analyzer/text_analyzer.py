def count_words(text: str) -> int:
    """Count words in text using specified separators."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text.strip():
        return 0

    separators = [' ', ',', ':', ';', '\t', '\n']
    for sep in separators:
        text = text.replace(sep, ' ')

    words = [word for word in text.split() if word]
    return len(words)