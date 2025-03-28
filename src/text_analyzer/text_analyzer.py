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


def count_sentences(text: str) -> int:
    """Count sentences in text using specified endings."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text.strip():
        return 0

    text = text.replace('...', '.')
    count = 0
    for char in text:
        if char in ['.', '!', '?']:
            count += 1
    return count