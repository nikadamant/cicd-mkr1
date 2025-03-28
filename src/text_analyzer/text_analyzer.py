from pathlib import Path

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


def analyze_file(file_path: str | Path) -> dict:
    """Analyze text file and return word and sentence counts."""
    if not isinstance(file_path, (str, Path)):
        raise TypeError("File path must be a string or Path object")

    # Convert Path to string if needed
    file_path_str = str(file_path)

    if not file_path_str.endswith('.txt'):
        raise ValueError("File must have .txt extension")

    try:
        with open(file_path_str, 'r', encoding='utf-8') as file:
            text = file.read()

        return {
            'words': count_words(text),
            'sentences': count_sentences(text)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path_str}")
    except PermissionError:
        raise PermissionError(f"Permission denied for file: {file_path_str}")
    except Exception as e:
        raise Exception(f"Error analyzing file: {str(e)}")